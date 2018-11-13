import pandas as pd 
import pymysql
from sqlalchemy import create_engine
from insert_report.op_package import op_pack
from insert_report.getInvention import getInventionMain

op_pack = op_pack()

# local test
# config = {"host": "10.209.152.109",
#           "user" : "root",
#           "passwd" : "123qwe",
#           "db" : "dbWafer",
#           "port" : 3306,
#           "charset" : "utf8"}
# engine = create_engine('mysql+pymysql://root:123qwe@10.209.152.109:3306/reportdata')

# production environment get reportdata database's engine
engine = create_engine(op_pack.get_reportEngine())


# production environment get_dbWaferConn
config = op_pack.get_dbWaferConn()


# engine = op_pack.get_reportEngine()
def addYield(phase, status, yield_cp, yield_assy, yield_mt, yield_ft):
    '''
    :param phase:
    :param status:
    :param yield_cp:
    :param yield_assy:
    :param yield_mt:
    :param yield_ft:
    :return: compound_field
    '''
    if phase == 'wafer' or (phase == 'cp' and status in('run', 'hold')) or (phase == 'assy' and status == 'wbank'):
        return yield_cp*yield_assy*yield_mt*yield_ft
    if (phase == 'cp' and status in ('fg', 'ship')) or (phase == 'assy' and status in('wait', 'run', 'hold')):
        return yield_assy*yield_mt*yield_ft
    if (phase == 'assy' and status in ('fg', 'ship')) or (phase == 'mt' and status in ('run', 'hold')):
        return yield_mt*yield_ft
    if (phase == 'mt' and status == 'ship') or (phase == 'ft'):
        return yield_ft

def addKgd_bak(df_wbank):
    if df_wbank['kgd'] == 'kgd':
        return df_wbank['bank']
    else:
        return 0

def addWait(df_wbank):
    if df_wbank['Phase'] == 'diebank' and df_wbank['kgd'] != 'kgd':
        return df_wbank['bank']
    else:
        return 0

def addWbank(df_wbank):
    if df_wbank['Phase'] == 'bank' and df_wbank['kgd'] != 'kgd':
        return df_wbank['bank']
    else:
        return 0
def addCompound(df_latest):
    '''
    add compound column: compound_field, compound_gross;
    modify two column: phase and grossdie
    '''
    df_latest.loc[~df_latest['Phase'].isin(['wafer', 'cp', 'bank']), 'gross_die'] = 1
    df_latest.loc[df_latest['Phase'].isin(['diebank', 'bank']), 'Phase'] = 'assy'
    df_latest['compound_field'] = df_latest.apply(lambda row: addYield(row['Phase'], row['status'],
                                                                              row['yield_cp'], row['yield_assy'],
                                                                              row['yield_mt'], row['yield_ft']), axis=1)
    df_latest['compound_gross'] = df_latest['quantity']*df_latest['gross_die']
    df_latest['datetime_str'] = df_latest['datetime_str'].map(str).str.strip()
    df_latest['datetime_str'] = pd.to_datetime(df_latest['datetime_str'])
    df_latest.rename(columns={'Phase': 'phase', 'PN': 'pn', 'datetime_str': 'receive_date'}, inplace=True)
    
    return df_latest
def dbHandle_data(df_data):
    '''
    Transfer Run, Hold, Fg, Wait, Bank to quantity and status
    '''
    df_run = df_data[df_data['Run'] != 0].copy()
    df_run.drop(['Hold', 'fg', 'wait', 'bank'], axis=1, inplace=True)
    df_run.rename(columns={'Run': 'quantity'}, inplace=True)
    df_run.insert(6, 'status', 'run')

    df_hold = df_data[df_data['Hold'] != 0].copy()
    df_hold.drop(['Run', 'fg', 'wait', 'bank'], axis=1, inplace=True)
    df_hold.rename(columns={'Hold': 'quantity'}, inplace=True)
    df_hold.insert(6, 'status', 'hold')

    df_fg = df_data[df_data['fg'] != 0].copy()
    df_fg.drop(['Run', 'Hold', 'wait', 'bank'], axis=1, inplace=True)
    df_fg.rename(columns={'fg': 'quantity'}, inplace=True)
    df_fg.insert(6, 'status', 'fg')

    df_bank = df_data[df_data['bank'] != 0].copy()
    df_bank['kgd_bank'] = df_bank.apply(addKgd_bak, axis=1)
    df_bank['wait'] = df_bank.apply(addWait, axis=1)
    df_bank['wbank'] = df_bank.apply(addWbank, axis=1)
    # df_bank['Phase'] = 'assy'
    # df_kgd = df_bank[['product_family', 'PN', 'vendor', 'kgd_bank', 'report_date']]
    df_kgd_bank = df_bank[df_bank['kgd_bank'] != 0].copy()
    df_kgd_bank.loc[df_kgd_bank['Phase'].isin(['diebank', 'bank']), 'Phase'] = 'assy'
    df_kgd = df_kgd_bank[['product_family', 'PN', 'vendor', 'Phase', 'kgd_bank', 'report_date']]
    df_kgd = df_kgd.rename(columns={"PN": "pn", "Phase": "phase"})
    df_bank.drop(['Run', 'Hold', 'fg', 'bank', 'kgd_bank'], axis=1, inplace=True)
    df_wait = df_bank[df_bank['wait'] != 0].copy()
    df_wait.drop(['wbank'], axis=1, inplace=True)
    df_wait.rename(columns={'wait': 'quantity'}, inplace=True)
    df_wait.insert(6, 'status', 'wait')
    df_wbank = df_bank[df_bank['wbank'] != 0].copy()
    df_wbank.drop(['wait'], axis=1, inplace=True)
    df_wbank.rename(columns={'wbank': 'quantity'}, inplace=True)
    df_wbank.insert(6, 'status', 'wbank')
    df_latest = pd.concat([df_run, df_hold, df_fg, df_wait, df_wbank], ignore_index=True, sort=True)
    return df_kgd, df_latest



def handle_filData(df_data, cursor):
    '''
    Add column pf, fpn, and from table pn_list to get yield information
    '''
    series_pf = pd.Series()
    series_fpn = pd.Series()
    series_grossdie = pd.Series()
    series_yieldcp = pd.Series()
    series_yield_assy = pd.Series()
    series_yield_mt = pd.Series()
    series_yield_ft = pd.Series()
    for i in range(len(df_data)):
        pn = df_data.loc[i ,'PN']
        phase = df_data.loc[i, 'Phase']
        if df_data.loc[i, 'err'] == 1:
            series_pf.loc[i] = series_fpn.loc[i] = 'UNCLASSIFIED'
            series_grossdie.loc[i] = series_yieldcp.loc[i] = series_yield_assy.loc[i] = series_yield_mt.loc[i] = series_yield_ft.loc[i] = 1
            continue
        if df_data.loc[i, 'kgd'] == 'kgd':
            sql = f"SELECT sales_kgd_pn,sales_product_family, gross_die FROM pn_list WHERE  kgd_pn= '{pn}'"
        elif phase == 'wafer':
            sql = f"SELECT product_family, sales_product_family, gross_die FROM pn_list WHERE product='{pn}'"
        elif phase == 'cp':
            sql = f"SELECT product_family, sales_product_family, gross_die FROM pn_list WHERE cp_pn='{pn}' OR product='{pn}'"
        elif phase in ('diebank', 'bank'):
            sql = f"SELECT product_family, sales_product_family, gross_die FROM pn_list WHERE '{pn}' in (cp_pn, product, assy_pn, ft_pn, untested_wafer_pn)"
        elif phase == 'assy' and df_data.loc[i, 'bank'] == 0:
            sql = f"SELECT ext_pn,sales_product_family, gross_die FROM pn_list WHERE '{pn}' in (cp_pn, product, assy_pn, ft_pn, untested_wafer_pn)"
        elif phase == 'mt':
            sql = f"SELECT ext_pn,sales_product_family, gross_die FROM pn_list WHERE '{pn}' in (mt_pn, assy_pn)"
        elif phase == 'ft':
            sql = f"SELECT ext_pn,sales_product_family, gross_die, ft_pn FROM pn_list WHERE '{pn}' in (ft_pn, mt_pn, assy_pn, ext_pn)" 
        cursor.execute(sql)
        data = cursor.fetchone()
        series_pf.loc[i] = data[1]
        series_fpn.loc[i] = data[0]
        series_grossdie.loc[i] = data[2]
        if phase == 'ft':
            pn = data[3]
        if phase in ('wafer', 'cp', 'diebank', 'bank'):
            sqlyield = f"SELECT cp,assembly,mt,ft FROM yield WHERE product_family='{series_pf[i]}'" 
        else:
            sqlyield = f"SELECT cp,assembly,mt,ft FROM yield WHERE full_part_number= '{series_fpn[i]}'"
        cursor.execute(sqlyield)
        yieldData = cursor.fetchone()
        if not yieldData:
            series_yieldcp.loc[i] = series_yield_assy.loc[i] = series_yield_mt.loc[i] = series_yield_ft.loc[i] = 1
        else:
            series_yieldcp.loc[i], series_yield_assy.loc[i], series_yield_mt.loc[i], series_yield_ft.loc[i] = yieldData[0], yieldData[1], yieldData[2], yieldData[3]
    df_data.insert(0, 'product_family', series_pf)
    df_data.insert(1, 'full_part_number', series_fpn)
    df_data['gross_die'] = series_grossdie
    df_data['yield_cp'], df_data['yield_assy'], df_data['yield_mt'], df_data['yield_ft'] =series_yieldcp, series_yield_assy, series_yield_mt, series_yield_ft
    return dbHandle_data(df_data)
            
def cur_getFilterData(connection):
    create_tmp = '''CREATE TEMPORARY TABLE tmp_filtered SELECT a.* from filtered_data a INNER JOIN (SELECT ori_table, MAX(datetime_str)datetime_str from filtered_data GROUP BY ori_table)b on a.ori_table=b.ori_table
AND a.datetime_str=b.datetime_str'''
    sel_combined = '''SELECT PN, vendor, Phase,SUM(Run)Run, SUM(Hold)Hold, SUM(FG)fg, SUM(Wait)wait, SUM(Bank)bank, AVG(Err)err, KGD kgd, report_date, datetime_str 
FROM tmp_filtered GROUP BY PN, vendor, Phase ORDER BY ID'''
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # cursor.execute("DROP TABLE IF EXISTS tmp_filtered")
            cursor.execute(create_tmp)
            connection.commit()
            df_filterData = pd.read_sql_query(sel_combined, connection)

        # 对读取到合并后的Run，Hold等的表进行处理
            # df_latestReport = handle_filData(df_filterData, cursor)
            df_kgd, df_latestReport = handle_filData(df_filterData, cursor)
            df_latest = addCompound(df_latestReport)
            df_latest = df_latest[['product_family', 'full_part_number', 'pn', 'vendor', 'phase', 'quantity', 
                                   'status', 'gross_die', 'yield_cp', 'yield_assy', 'yield_mt', 'yield_ft', 
                                   'compound_field', 'compound_gross', 'report_date', 'receive_date']]
            # get inventory and concat inventory and latest
            df_invention, df_ship, df_shipKgd = getInventionMain()
            df_latestMain = pd.concat([df_latest, df_invention, df_ship], ignore_index=True, sort=True)
            if len(df_shipKgd):
                df_kgd = pd.concat([df_kgd, df_shipKgd], ignore_index=True, sort=True)
            # print(df_kgd)
            print('latest条数:', len(df_latest),'   ', 'invention条数:', len(df_invention))
            print(df_latestMain)
    except Exception as e:
        raise e
    finally:
        # connection.close()
        pass
    conn = engine.raw_connection()
    try:
        cur = conn.cursor()
        cur.callproc("delete_latestSimply", args=())
        cur.callproc("delete_kgd_bank_tbl", args=())
        cur.close()
        conn.commit()
    except Exception:
        raise
    finally:
        conn.close()
    df_latestMain.to_sql('latestSimply', engine, if_exists='append', index=False)
    df_kgd.to_sql('kgd_bank_tbl', engine, if_exists='append', index=False)

def filterToLatestMain(connection=''):
    # getConnection and deal with the table from mysql database
    cur_getFilterData(connection)

if __name__ == '__main__':
    filterToLatestMain()

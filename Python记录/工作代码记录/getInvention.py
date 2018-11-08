import pandas as pd
import pymysql
import threading
import time
import datetime
from insert_report.op_package import op_pack

__all__ = ('getInventionMain',)
df_data = pd.DataFrame()
df_ship = pd.DataFrame()
df_shipKgd = pd.DataFrame()
op_pack = op_pack()


def handle_invent(df_invent, df_pnList):
    df_invent_pn = pd.merge(df_invent, df_pnList, how='left', left_on='pn', right_on='ft_pn')
    df_invent_pn.fillna('UNCLASSIFIED', inplace=True)
    df_invent_pn.rename(columns={'sales_product_family': 'product_family'}, inplace=True)
    df_pn_invent = df_invent_pn[['product_family', 'full_part_number', 'pn', 'quantity']].copy()
    df_pn_invent.loc[:, 'vendor'] = 'HK.CAY'
    df_pn_invent.loc[:, 'phase'] = 'inventory'
    df_pn_invent.loc[:, 'status'] = 'inventory'
    df_pn_invent.loc[:, 'gross_die'] = df_pn_invent.loc[:, 'yield_cp'] = df_pn_invent.loc[:, 'yield_assy'] = df_pn_invent.loc[:, 'yield_mt'] = \
    df_pn_invent.loc[:, 'yield_ft'] = df_pn_invent.loc[:, 'compound_field'] = 1
    df_pn_invent.loc[:, 'compound_gross'] = df_pn_invent["quantity"]*df_pn_invent["gross_die"]
    df_pn_invent.loc[:, 'report_date'] = datetime.date.today()
    df_pn_invent.loc[:, 'receive_date'] = datetime.datetime.now()
    cols = list(df_pn_invent.columns)
    # print(cols)
    cols = cols[:3] + cols[4:6] + cols[3:4] + cols[6:]
    df_pn_invent = df_pn_invent[cols]
    return df_pn_invent


def get_df_PnList(config):
    pnListSql = "SELECT sales_product_family, product, ext_pn, ft_pn, sales_ext_pn FROM pn_list"
    connection = pymysql.connect(**config)
    df_pnList = pd.read_sql_query(pnListSql, connection)
    connection.close()
    return df_pnList


def get_invention(config):
    connection = pymysql.connect(**config)

    # dbWafer的连接字符串 use test
    # dbWaferConn = {"host": "10.209.152.109",
    #                "user": "root",
    #                "passwd": "123qwe",
    #                "db": "dbWafer",
    #                "port": 3306,
    #                "charset": "utf8"
    #                }
    dbWaferConn = op_pack.get_dbWaferConn()
    inventSql = "SELECT b.Item pn, b.PN full_part_number,sum(a.TotalQTY) quantity from inventory a INNER JOIN \
    productinfo b on a.PN=b.ID where a.Warehouse=42 and a.TotalQTY != 0 GROUP BY a.PN ORDER BY a.ID"
    # 获取inventory数据
    df_invent = pd.read_sql_query(inventSql, connection)
    # print(df_invent)
    # 获取pnList中的数据
    df_pnList = get_df_PnList(dbWaferConn)
    # print(df_pnList)
    # 生成需要拼接到simplyLatest中的df
    df_invention = handle_invent(df_invent, df_pnList)

    # 赋值给全局变量
    global df_data
    df_data = df_invention
    connection.close()

def get_aseShip(cur):
    df_aseShip = pd.DataFrame(columns=['product_family', 'full_part_number', 'pn', 'quantity', 'report_date', 'receive_date'])
    cur.execute(f"SELECT * FROM assly_ase_ship where report_date = '2018-10-22'")
    aseShipDatas = cur.fetchall()
    receive_date = pd.to_datetime(aseShipDatas[0][-1])
    for i, item in enumerate(aseShipDatas):
        cur.execute(f"SELECT sales_product_family, ext_pn FROM pn_list where assy_pn = '{item[15]}'")
        pfDatas = cur.fetchone()
        if pfDatas:
            print(pfDatas)
            df_aseShip.loc[i] = [pfDatas[0], pfDatas[1], item[15], item[4], aseShipDatas[0][-2], receive_date]
        else:
            df_aseShip.loc[i] = ['UNCLASSIFIED', 'UNCLASSIFIED', item[15], item[4], aseShipDatas[0][-2], receive_date]
        return df_aseShip
    cur.close()

def addYield(cur, df_shipData, i):
    if df_shipData.loc[i, 'phase'] in ('wafer', 'cp'):
        sqlyield = f"SELECT cp,assembly,mt,ft FROM yield WHERE product_family='{df_shipData.loc[i, 'product_family']}'"
    else:
        sqlyield = f"SELECT cp,assembly,mt,ft FROM yield WHERE full_part_number= '{df_shipData.loc[i, 'full_part_number']}'"
    cur.execute(sqlyield)
    yieldData = cur.fetchone()
    if yieldData:
        df_shipData.loc[i, 'yield_cp'], df_shipData.loc[i, 'yield_assy'],  \
            df_shipData.loc[i, 'yield_mt'], df_shipData.loc[i, 'yield_ft'] = \
        yieldData[0], yieldData[1], yieldData[2], yieldData[3]
    else:
        df_shipData.loc[i, 'yield_cp'] = df_shipData.loc[i, 'yield_assy'] = \
            df_shipData.loc[i, 'yield_mt'] = df_shipData.loc[i, 'yield_ft'] = 1


def fill_excelShip(df_ship):
    df_ship['status'] = 'ship'
    df_ship['compound_field'] = df_ship['yield_cp']*df_ship['yield_assy']* \
                                df_ship['yield_mt']*df_ship['yield_ft']
    df_ship.loc[~df_ship['phase'].isin(['wafer', 'cp', 'kgd']), 'gross_die'] = 1
    df_ship['compound_gross'] = df_ship['quantity']*df_ship['gross_die']
    df_ship['report_date'] = datetime.date.today()
    df_ship['receive_date'] = datetime.datetime.now()
    df_shipKGD, df_ship = df_ship[df_ship['phase'] == 'kgd'], df_ship[df_ship['phase'] != 'kgd']
    df_ship = df_ship[['product_family', 'full_part_number', 'pn', 'vendor', 'phase', 'quantity',
                        'status', 'gross_die', 'yield_cp', 'yield_assy', 'yield_mt', 'yield_ft',
                         'compound_field', 'compound_gross', 'report_date', 'receive_date']]
    if len(df_shipKGD):
        print("********df_shipKGD", df_shipKGD)
        df_shipKGD = df_shipKGD[['product_family', 'pn', 'vendor', 'phase', 'compound_gross', 'report_date']]
        df_shipKGD.rename(columns={'compound_gross': 'kgd_bank'}, inplace=True)
        global df_shipKgd
        df_shipKgd = df_shipKGD
    return df_ship

def get_excelShip(cur):
    stockInPath = op_pack.get_StockInPath()
    # stockInPath = "insert_report/Stock in transit.xlsx"
    print(stockInPath)
    df_excelShip = pd.read_excel(stockInPath)
    df_shipRecord = df_excelShip[df_excelShip["Recive_Date"] == 'SHIP'].copy()
    df_shipRecord.reset_index(drop=True, inplace=True)
    df_shipRecord.columns = df_shipRecord.columns.str.strip()
    df_shipRecord['From'] = df_shipRecord['From'].str.lower()
    df_shipRecord['Phase'] = df_shipRecord['Phase'].str.lower()
    df_ship = df_shipRecord[["Foundry_P/N", "AVL_P/N", "From","Phase", "Qty"]].copy()
    df_ship.rename(columns={"Foundry_P/N": "pn", "AVL_P/N": "full_part_number", "From": "vendor", "Qty": "quantity", "Phase":"phase"}, inplace=True)

    for i in range(len(df_ship)):
        pfSql = f"SELECT sales_product_family, gross_die from pn_list where '{df_ship.loc[i, 'full_part_number']}' in (cp_pn, product, assy_pn, ft_pn, mt_pn, ext_pn)"
        cur.execute(pfSql)
        pfData = cur.fetchone()
        if pfData:
            df_ship.loc[i, 'product_family'] = pfData[0]
            df_ship.loc[i, 'gross_die'] = pfData[1]
            addYield(cur, df_ship, i)
        else:
            df_ship.loc[i, 'product_family'] = 'UNCLASSIFIED'
            df_ship.loc[i, 'gross_die'] = 1
            df_ship.loc[i, 'yield_cp'] = df_ship.loc[i, 'yield_assy'] = \
                df_ship.loc[i, 'yield_mt'] = df_ship.loc[i, 'yield_ft'] = 1
    return fill_excelShip(df_ship)

def fillup_df(df_aseShip):
    df_aseShip.insert(3, 'vendor', 'ase')
    df_aseShip.insert(4, 'phase', 'ship')
    df_aseShip['status'] = 'ship'
    df_aseShip['gross_die']=df_aseShip['yield_cp']=df_aseShip['yield_assy']=df_aseShip['yield_mt']= \
    df_aseShip['yield_ft']=df_aseShip['compound_field']=df_aseShip['compound_gross']=1
    cols = list(df_aseShip.columns)
    cols = cols[:6] + cols[8:] + cols[6:8]
    df_aseShip = df_aseShip[cols]
    return df_aseShip

def getShip():
    waferConn = op_pack.get_dbWaferConn()
    waferConnection = pymysql.connect(**waferConn)
    waferCur = waferConnection.cursor()
    # 将ship分为三个部分
    # df_aseShip = get_aseShip(waferCur)
    # getHKShip()
    # getOtherShip()

    # 读取excel中的ship
    df_excelShip = get_excelShip(waferCur)

    # df_Ship = fillup_df(df_excelShip)
    print(df_excelShip)
    # 赋值给全局变量
    global df_ship
    df_ship = df_excelShip
    # return df_excelShip

def getInventionMain():
    # use test
    # inventConn = {"host": "10.209.152.110",
    #               "user": "inventory",
    #               "passwd": "inventory",
    #               "db": "psi",
    #               "port": 3309,
    #               "charset": "utf8"}
    inventConn = op_pack.get_InventConn()
    t_invent = threading.Thread(target=get_invention, args=(inventConn,))
    t_ship = threading.Thread(target=getShip, args=())
    t_invent.start()
    t_ship.start()
    # df_ship = getShip()
    t_invent.join()
    t_ship.join()
    print (df_data, df_ship)
    print("df_shipKgd", df_shipKgd)
    return df_data, df_ship, df_shipKgd

if __name__ == "__main__":
    getInventionMain()
import pymysql

config = {
    "host":'10.209.152.111', 
    "port":3306, 
    "user":'root', 
    "passwd":'Avl1108', 
    "db":'hdcp'
}
test_config = {
    "host":'10.209.152.209', 
    "port":3306, 
    "user":'hdcp', 
    "passwd":'Avl_1108', 
    "db":'hdcp'
}
def doSelectHdcp():
    connection = pymysql.connect(**config)
    connection_test = pymysql.connect(**test_config)

    cur = connection.cursor()
    cur_test = connection_test.cursor()

    for j in range(10000):
        selSql = f"select id, value, is_use from 2x_rx limit 1000"

        cur.execute(selSql)

        selData = cur.fetchall()
        for i, item in enumerate(selData):
            insertSql = f"insert into 2x_rx_back(id, value, is_use) values ({item[0]}, '{item[1]}', '{item[2]}')" 
            # print(insertSql)
            cur_test.execute(insertSql)
            if i % 1000==0:
                connection_test.commit()
        connection_test.commit()
        m=j+1
        print("完成记录:", m*1000)
        cur.execute("DELETE from 2x_rx where 1=1 LIMIT 1000")
        connection.commit()
        print('删除.109记录',m*1000)

    cur.close()
    cur_test.close()
    connection.close()
    connection_test.close()
    print("完成:")

if __name__=='__main__':
    doSelectHdcp()
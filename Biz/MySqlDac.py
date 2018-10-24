import pymysql

def getAllMaterial(mon):
    conn,curs = getConn()
    sql = 'select * from month_material where month = ' + str(mon)
    count = curs.execute(sql)
    res = curs.fetchall()
    conn.commit()
    conn.close()
    return res

def getConn():
    conn = pymysql.connect(host='35.238.55.16', user='root', password='yoriyori',
                           db='yoriyori', charset='utf8')
    curs = conn.cursor()
    return conn,curs
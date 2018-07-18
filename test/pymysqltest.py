import pymysql

host = '115.159.193.122'
port = 3306
username = 'root'
password = 'hkxx@206'
db = 'cola'
charset = 'utf8'

conn = pymysql.connect(host=host,
                       port=port,
                       user=username,
                       password=password,
                       db=db,
                       charset=charset,
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

sql = 'select * from illbaike'
cursor.execute(sql)
# cursor.fetchall()
print(cursor.rowcount)

conn.commit()


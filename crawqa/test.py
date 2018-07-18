import pymysql

with open('links.txt', 'r') as fin:
	st = fin.read()

lst = st.split('*')
print(len(lst))

lst_copy = []
for link in lst:
	if link in lst_copy:
		continue
	else:
		lst_copy.append(link)
print(len(lst_copy))

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
sql = 'insert into linkstat(link, ifcrawed) values(%s, %s)'

for link in lst_copy:
	cursor.execute(sql, [link, 0])
	conn.commit()

conn.close()

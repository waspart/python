# 向mysql数据表中插入数据
# 儿童类节目单独处理
import pymysql
import os
import xlrd

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
sql = r'insert into himalayanAlbum(`albumId`, `albumName`, ' +\
      '`albumClass`, `albumTag`) values(%s, %s, %s, %s, %s, %s)'

_path = r'D:\python\excelprocess\xlsxs\儿童专辑总表'
workbook = xlrd.open_workbook(_path)
# 获取该文件中所有表格名称
sheetnames = workbook.sheet_names()
print('文件名称：', _path, '表格数量：', len(sheetnames))
# 循环处理当前文件中所有表格
for sname in sheetnames:
    sheet = workbook.sheet_by_name(sname)
    for sname in sheetnames:
        # 获取当前文件中当前表格内容
        sheet = workbook.sheet_by_name(sname)
        # print(sheet.row_values(1), len(sheet.row_values(1)))
        # print(sheet.nrows)
        for i in list(range(2, sheet.nrows)):
            # print(i)
            dat = sheet.row_values(i)
            cursor.execute(sql, dat)
    print('最新插入记录ID编号：', int(conn.insert_id()))
    conn.commit()




cursor.close()
conn.close()



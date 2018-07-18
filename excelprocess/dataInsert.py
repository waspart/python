# 向mysql数据表中插入数据
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
      '`albumClass`, `albumTag`, `playNo`, `anchorName`) ' +\
      'values(%s, %s, %s, %s, %s, %s)'

_path = r'D:\python\excelprocess\xlsxs'
# 读取出文件中所有文件名称
lst_file = os.listdir(_path)
# print(len(lst_file))

# 循环处理每一个文件内容
for file in lst_file:
    # 打开当前文件
    workbook = xlrd.open_workbook(_path + os.sep + file)
    # 获取该文件中所有表格名称
    sheetnames = workbook.sheet_names()
    # 打印文件信息
    print('文件名称：', file, '表格数量：', len(sheetnames))
    # 循环处理当前文件中所有表格
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
print('Done!!!!!!!!!!!!')



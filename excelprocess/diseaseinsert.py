import os
import pymysql
import xlrd

_path = r'xlsxs/'

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

insert_sql = 'insert into diseases(disease, question, answer) values(%s, %s, %s)'

file_lst = os.listdir(_path)
# print(len(file_lst))
for filename in file_lst:
    dname = filename.split('.')[0]
    file_path = _path + filename
    # print(file_path)

    if dname not in ['乳腺疾病']:
        continue

    # print('疾病名称：', dname, end='  ')

    wbook = xlrd.open_workbook(file_path)
    sheetname = wbook.sheet_names()[0]
    sheetcont = wbook.sheet_by_name(sheetname)

    for i in list(range(sheetcont.nrows))[1:]:
        this_line = sheetcont.row_values(i)
        data = []
        data.append(dname)

        if this_line[0].strip() == '' or this_line[1].strip() == '':
            continue

        print('processing.......', end='  ')

        this_question = this_line[0].strip().replace('\n', '')
        this_question = this_question.replace(' ', '')
        data.append(this_question)
        this_answer = this_line[1].strip().replace('\n', '')
        this_answer = this_answer.replace(' ', '')
        data.append(this_answer)

        cursor.execute(insert_sql, data)
        print('插入第', repr(cursor.lastrowid), '条数据', 'Done!!!!!!!!!')
        conn.commit()



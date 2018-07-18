import os
import pymysql
import xlrd

def judgec(lst):
    if lst[2] - lst[1] == 1 and lst[1] - lst[0] == 0:
        return True
    return False

def judgel(lst):
    for i in list(range(len(lst)))[:-2]:
        isc = judgec(lst[i:i+3])
        if isc:
            return True
    return False

_path = r'xlsxs/慢支.xlsx'

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

wbook = xlrd.open_workbook(_path)
sheetname = wbook.sheet_names()[0]
sheetcont = wbook.sheet_by_name(sheetname)

index_0 = [0]
index_s = []
count = 0
for i in list(range(sheetcont.nrows))[1:]:
    this_line = sheetcont.row_values(i)
    line_0 = this_line[0]
    if line_0.strip() == '':
        index_0.append(0)
    else:
        index_0.append(1)
        index_s.append(i)
        count += 1
# print(count)
# print(index_0)
# print(len(index_0))
# print(len(index_s))
# print(index_s)
# print(judgel(index_s))
index_s.append(sheetcont.nrows)
# print(len(index_s))
# print(sheetcont.nrows)

for i in list(range(len(index_s)))[1:-1]:
    cno = 0
    ind = 0
    data = []
    data.append('慢支')

    # print(i, end='  ')
    if i < len(index_s) - 1:
        if index_s[i + 1] - index_s[i] == 1:
            continue

    if index_s[i] - index_s[i - 1] == 1:
        ind = i - 1
        cno = 2
    else:
        ind = i
        cno = 1

    # print('ind :', ind)
    this_question = ''
    # print(1, ind, index_s[ind], index_s[ind] + cno, end=' ')
    for j in list(range(index_s[ind], index_s[ind] + cno)):
        this_line = sheetcont.row_values(j)
        cont = this_line[0].strip().replace('\n', '')
        cont = cont.replace(' ', '')
        this_question += cont
    data.append(this_question)
    # print(j)

    this_answer = ''
    # print(2, ind, len(index_s), index_s[ind], index_s[ind + 1], sheetcont.nrows, end=' ')
    for j in list(range(index_s[ind], index_s[ind + 1])):
        this_line = sheetcont.row_values(j)
        cont = this_line[1].strip().replace('\n', '')
        cont = cont.replace(' ', '')
        this_answer += cont
    data.append(this_answer)
    # print(j)

    # print(i, end='  ')
    # print(data)

    cursor.execute(insert_sql, data)
    print('插入第', repr(cursor.lastrowid), '条数据', 'Done!!!!!!!!!')
    conn.commit()




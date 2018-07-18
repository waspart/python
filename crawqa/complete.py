import pymysql
import time
import re

vswf = re.compile(u'[\u4e00-\u9fa5]+')

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

select_sql = 'select id, question, coretip, answer from illbaike limit %s, %s'
update_sql = 'update illbaike set question=%s, coretip=%s, answer=%s where id=%s'
delete_sql = 'delete from illbaike where id=%s'

nolst = list(range(0, 6050, 100))
nolst.append(6050)
n = 100
count = 0

for no in nolst:
    if 6050 - no < 100:
        n = 6050 - no

    cursor.execute(select_sql, (no, n))
    for qa in cursor.fetchall():
        # print()
        deleteFlag = False
        id = qa['id']
        question = qa['question'].strip()
        coretip = qa['coretip'].strip()
        answer = str(qa['answer'], encoding='utf-8').strip()

        # question = question.replace(' ', '').replace('\r', '').replace('\n', '').encode('iso-8859-1').decode('gbk')
        # coretip = coretip.encode('iso-8859-1').decode('gbk')
        # answer = answer.replace(' ', '').replace('\r', '').replace('\n', '').encode('utf-8').decode('iso-8859-1')
        # answer = answer.encode('iso-8859-1').decode('gbk')

        # print('问题是：{}'.format(question))
        # print('提示是：{}'.format(coretip))
        # print('答案是：{}'.format(answer))

        if coretip == '' and question == '' and answer == '':
            deleteFlag = True
        # print(len(question), len(coretip), len(answer))

        if coretip != '':
            lst = coretip.split('：')
            # print(lst)
            if '核心提示' not in lst:
                # continue
                # print('Yes')
            # else:
                deleteFlag = True
                # cursor.execute(delete_sql, id)
                # conn.commit()
                # print('no')
        else:
            if not vswf.search(question):
                deleteFlag = True
            # print('no')

        # print(deleteFlag)
        if deleteFlag:
            print('编号是：{}，问题是：{}'.format(id, question))
            cursor.execute(delete_sql, id)
            conn.commit()
            count += 1
            # time.sleep(0)

print(count)
conn.close()

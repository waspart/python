import pymysql
import requests
from bs4 import BeautifulSoup
import time
import random

def get_cont(url):
	head = {
		'user-agent': 'Mozail/5.0'
	}
	html_cont = requests.get(url, timeout=60, headers=head)
	if html_cont.status_code == 200:
		return html_cont.content
	else:
		return -1

def parse(html_cont):
	title_h1 = ""
	summary = ""
	cont = ""

	soup = BeautifulSoup(html_cont, 'html.parser')
	main_cont = soup.find('div', class_='art_box')

	if main_cont is not None:
		if main_cont.find('h1') is not None:
			title_h1 = main_cont.find('h1').text
		if main_cont.find('p', class_='summary') is not None:
			summary = main_cont.find('p', class_='summary').text

		art_cont = main_cont.find('div', class_='art_con')
		lst_p = art_cont.find_all('p')
		for p in lst_p:
			if '相关推荐' in p.text.split('【'):
				break
			cont += p.text
	else:
		main_cont = soup.find('div', class_='art_2_con')
		if main_cont is not None:
			if main_cont.find('h2') is not None:
				title_h1 = main_cont.find('h2').text
			if main_cont.find('p', class_='summary') is not None:
				summary = main_cont.find('p', class_='summary')

			lst_p = main_cont.find_all('p')
			for p in lst_p:
				if '相关推荐' in p.text.split('【'):
					break
				cont += p.text

	return title_h1, summary, cont




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
insert_sql = 'insert into illbaike(question, coretip, answer) values(%s, %s, %s)'
select_sql = 'select id, link, ifcrawed from linkstat limit %s, %s'
update_sql = 'update linkstat set ifcrawed = 1 where id = %s'

totalcount = 6143
lst_no = list(range(0, totalcount, 100))
lst_no.append(totalcount)
n = 100

for no in lst_no:
	if totalcount - no < 100:
		n = totalcount - no

	cursor.execute(select_sql % (no, n))
	for an in cursor.fetchall():
		print("processing......", end="  ")
		updateFlag = True
		# print(an, end="  ")
		id = an['id']
		ifcrawed = an['ifcrawed']
		link = an['link']

		if ifcrawed == 1 or link == '':
			continue
			updateFlag = False
			print("UNDO!!!!!!!!")

		insert_data = []

		if get_cont(link) == -1:
			continue
			updateFlag = False
			print("UNDO!!!!!!!!")
		else:
			html_cont = get_cont(link)

		title_h1, summary, cont = parse(html_cont)
		cursor.execute(insert_sql, (title_h1, summary, cont))
		conn.commit()
		print("成功插入第 {} 条数据，Done！！！！！！！！！！".format(cursor.lastrowid))

		if updateFlag:
			cursor.execute(update_sql, id)
			conn.commit()

		time.sleep(abs(random.random() - 2))

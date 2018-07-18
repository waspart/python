import requests
from bs4 import BeautifulSoup
import sqlproc
import time

host = '115.159.193.122'
port = 3306
username = 'root'
password = 'hkxx@206'
db = 'cola'
charset = 'utf8'

sp = sqlproc.SqlProc(host, port, username, password, db, charset)
insert_sql = 'insert into linkstat(link, ifcrawed) values(%s, %s)'

root_url = r'http://www.baikemy.com/jiankangkepu/list/1?pageIndex='
lst_link = []
head = {
	'user-agent': 'myapp/1.0'
}


for i in list(range(192,193)):
	print('\n###########################################')
	print('#### 第{}页数据正在处理......'.format(i))
	print('###########################################')
	url = root_url + repr(i) + '&pageCount=193'
	req = requests.get(url, headers=head)
	if req.status_code != 200:
		continue

	soup = BeautifulSoup(req.text, 'html.parser')
	div_art = soup.find('div', class_='list_art')
	lst_art = div_art.find_all('div', class_='l_li_l')

	for art in lst_art:
		print('processing......', end="  ")
		link = 'http://www.baikemy.com' + art.find('a')['href']
		if link not in lst_link:
			bs, code = sp.insertData(insert_sql, (link, 0))
			if bs:
				print('插入成功！ 第 {} 条数据'.format(code), end="  ")
				lst_link.append(link)
			else:
				print('插入失败！', end="  ")
		else:
			print('该链接已经存在！')
			continue
		print('Done!!!!')

	time.sleep(2)

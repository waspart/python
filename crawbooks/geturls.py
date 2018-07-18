'''
获取小学书籍有用
'''

import requests
from bs4 import BeautifulSoup

url = r'https://www.ruiwen.com/jiaocai/yuwen/'

head = {
	'user-agent': 'myapp/1.0'
}
res = requests.get(url, timeout=30, headers=head)
soup = BeautifulSoup(res.text, 'html.parser')

lst_top_news = soup.find_all('div', class_='top_news')

for top_new in lst_top_news[1:4]:
	fin = open('top_links.txt', 'a+')
	# print('#######################')
	title = top_new.find('div', class_='comtitle').find('a').text
	fin.write('#' + title.encode('iso-8859-1').decode('utf-8'))
	# print('title: ', title.encode('iso-8859-1').decode('utf-8'))
	lst_pic_right = top_new.find_all('div', class_='pic_right')

	for pic_right in lst_pic_right:
		lst_li = pic_right.find_all('li')
		for li in lst_li:
			fin.write('*' + li.find('a')['href'])
			# print(li.find('a')['href'])

	fin.close()
	# print('#######################')

# 分离读取
fread = open('top_links.txt', 'r')
lst_ver = fread.read().split('#')
for ver in lst_ver:
	for link in ver.split('*'):
		print(link)



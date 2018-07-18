'''提取现有html文件中所有可提取的URL'''

import os
from bs4 import BeautifulSoup

_path = 'baike'
count = 0

lst_folder = os.listdir(_path)
# print(lst_folder)
# print('排序后：')
# print(lst_folder.sort())

for folder in lst_folder:
	this_folder = _path + os.sep + folder
	if len(os.listdir(this_folder)) > 0:
		html_index = this_folder + os.sep + 'index.html'
		print("正在查找：{}".format(html_index))
		count += 1

		with open(html_index, 'rb') as fread:
			html_cont = fread.read()

		soup = BeautifulSoup(html_cont, 'html.parser')
		# print(len((soup.find_all('div', class_='entry-list'))))
		# lst_item = soup.find('div', class_='entry-list').find_all('a')
		lst_item = soup.find('div', class_='entry-list').find_all('a')
		print("item 数量为 {}".format(len(lst_item)))

		for item in lst_item:
			link = item['href']
			if 'baike' in link.split('/') or 'disease' in link.split('/'):
				continue
			print(item['href'])
			with open('links.txt', 'a+') as fin:
				fin.write('*' + link)

	# if count == 2:
	# 	break

# print("总数量为 {}".format(count))


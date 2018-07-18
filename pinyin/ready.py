import requests
from bs4 import BeautifulSoup

url_pre = 'http://cd.hwxnet.com/'
url = 'http://cd.hwxnet.com/pinyin.html'
head = {'user-agent': 'Mozila/5.0'}
totalcount = 0

try:
	res = requests.get(url, headers=head, timeout=10)
	if res.status_code == 200:
		# print('')
		soup = BeautifulSoup(res.text, 'html.parser')
		level_1 = soup.find('div', class_='sub_con').find_all('a')
		print('一级链接数量：{}'.format(len(level_1)))
		# set_level_1 = set()
		for le in level_1:
			href = url_pre + le['href']
			print('#### 一级链接：{}'.format(href))
			# set_level_1.add(href)
			res_2 = requests.get(href, headers=head, timeout=10)
			if res_2.status_code == 200:
				# print()
				soup_2 = BeautifulSoup(res_2.text, 'html.parser')
				pys = soup_2.find('dl', class_='pinyin_dl').find_all('a')
				print('##\t 二级链接数量：{}'.format(len(pys)))
				for py in pys:
					py_link = url_pre + py['href']
					totalcount += 1
					print('\t\t{}\t链接：{}'.format(totalcount, py_link))
					with open('pylink.txt', 'a+') as fin:
						fin.write(py_link + '*')

			else:
				print('二级捕获失败！')

	else:
		print('一级获取失败！')
except:
	print('捕获异常！')
finally:
	print('End!!!!')
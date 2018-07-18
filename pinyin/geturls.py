import requests
from bs4 import BeautifulSoup

with open('pylink.txt', 'r') as fin:
	pycont = fin.read()
	pylinks = pycont.split('*')[:-1]
	# print(len(pylinks))
	# print(pylinks[-1].strip())

head = {'user-agent': 'Mozila/5.0'}
totalcount = 0
url_pre = 'http://cd.hwxnet.com/'

try:
	for plink in pylinks:

		plink = plink[:-5] + '_1.html'
		# print('#\t新链接：{}'.format(plink))

		set_new_links = set()
		set_old_links = set()
		set_obj_links = set()
		set_new_links.add(plink)

		while len(set_new_links) != 0:

			purl = set_new_links.pop()
			set_old_links.add(purl)

			pcont = requests.get(purl, headers=head, timeout=10)
			if pcont is not None:
				soup = BeautifulSoup(pcont.text, 'html.parser')
				page_links = soup.find('div', class_='sub_con f12 lh_p22 center').find_all('a')
				
				for page_link in page_links:
					page_link = url_pre + page_link['href']
					# print(page_link)
					if page_link not in set_old_links and page_link not in set_new_links:
						set_new_links.add(page_link)

				cy_links = soup.find('ul', class_='pinyin_ul').find_all('a')
				# print(len(cy_links))
				for cy_link in cy_links:
					cy = url_pre + cy_link['href']
					# print(cy)
					set_obj_links.add(cy)
					totalcount += 1
					# print('{}\t{}'.format(totalcount, cy))

				while len(set_obj_links) > 0:
					with open('cylinks.txt', 'a+') as fin:
						cy = set_obj_links.pop()
						print('链接\t{}'.format(cy))
						fin.write(cy + '*')

except:
	print('出现异常！')

finally:
	print('总数：{}'.format(totalcount))
	print('END!!!')
# 提取某一个医院的科室信息
import requests
import urllib.parse
from bs4 import BeautifulSoup


url = r'http://yyk.99.com.cn/luyang/77807/'

header = {
    'user-agent': 'my-app/0.0.1'
}

html_cont = requests.get(url, headers=header, timeout=20).text

soup = BeautifulSoup(html_cont, 'html.parser')
kscont = soup.find('div', class_='hp_docks').find_all('li')

ksinfo = ''
count = 1
for ks in kscont:
	s = ks.find('a').text.strip()
	if count == 1:
		ksinfo += s
	else:
		ksinfo += ',' + s
	count += 1

print(ksinfo)



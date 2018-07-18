import requests
from bs4 import BeautifulSoup

headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
# url = r'http://www.whatismyip.com.tw/'
url = r'http://icanhazip.com/'
scount = 0
fcount = 0

f  = open('output.txt', 'r')
# print(f.readline())
while f.readline() is not None:
	ip = ''
	s = f.readline()
	lst = s.split('*')
	if len(lst) > 1:
		ip = lst[1]
		print('ip地址：{}'.format(lst[1]), end=" ")
	else:
		break
	pro = {
		'http': 'http://' + ip,
		'https': 'http://' + ip
	}
	try:
		res = requests.get(url, headers=headers, proxies=pro, timeout=3)
		soup = BeautifulSoup(res.text, 'html.parser')
		txt = soup.find('pre').text
		print('连接成功！返回内容：{}'.format(txt))
		scount += 1
	except:
		print('连接错误！')
		fcount += 1



f.close()
print('成功数量：{}，失败数量：{}'.format(scount, fcount))

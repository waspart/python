import requests
import random
from requests.adapters import HTTPAdapter

url = r'http://www.google.com.cn'
# url = r'http://www.whatismyip.com.tw/' # 返回IP地址
# url = r'http://icanhazip.com/'
# url = r'http://www.xicidaili.com/nn/3' # ip代理
# url = r'https://api.github.com/events' # GitHub时间线
headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# pro = {
# 	'http': 'http://183.145.204.172:3128',
# 	'https': 'http://183.145.204.172:3128'
# }
# print(pro)

try:
	req = requests.Session()
	req.mount('http://', HTTPAdapter(max_retires=3))
	req.mount('https://', HTTPAdapter(max_retires=3))
	req.get(url, headers=headers, timeout=1)
	# req = requests.get(url, headers=headers, timeout=1)
except requests.exceptions.Timeout:
	print('Timeout')
# req = requests.get(url, proxies={'https':random.choice(proxys)}, headers=headers)
# req = requests.get(url, proxies=pro, timeout=10)
# res = requests.get(req)
# print(res.apparent_encoding)
# print(req.encoding)
# print(req.text)
# print(req.headers)
print(req.status_code)



# encoding=utf8
import requests
import sys
from bs4 import BeautifulSoup

s = requests.session()
proxie = {
    'http': 'http://115.223.236.121:9000',
    'https': 'http://115.223.236.121:9000'
}
url = 'http://www.whatismyip.com.tw/'
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
}
# print(url)
response = s.get(url, headers=header, verify=False, proxies=proxie, timeout=10)
# response = s.get(url, headers=header, verify=False, timeout=10)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find('span').text.strip())

# print(response.text)
# f = open('FC.html','w')
# f.write(response.content)
# f.close()

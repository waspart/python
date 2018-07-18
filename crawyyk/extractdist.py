import requests
import urllib.parse
from bs4 import BeautifulSoup
# import os
# import time
# import re

root_url = 'http://yyk.99.com.cn/'

r = requests.get(root_url, timeout=20)
r.raise_for_status()
print('编码方式：', r.apparent_encoding)
print('返回码：', r.status_code)

html_cont = r.text

soup = BeautifulSoup(html_cont, 'html.parser')
dist = soup.find('div', class_='lcr_bottom')
# print(dist)

links = dist.find_all('li')
# print(links)
print(len(links))

fout = open('dists.txt', 'a+', encoding='utf-8')
for i in list(range(len(links))):
    fout.write(urllib.parse.urljoin(root_url, links[i].find('a')['href']) + '\n')

fout.close()





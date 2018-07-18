import requests
import urllib.parse
from bs4 import BeautifulSoup

url = 'http://yyk.99.com.cn/jiangsu/'

header = {
    'user-agent': 'my-app/0.0.1'
}


res = requests.get(url, timeout=20)
html_cont = res.text

soup = BeautifulSoup(html_cont, 'html.parser')
divs = soup.find_all('div', class_='tablist')

count = 0
for div in divs:
    links = div.find_all('li')

    for link in links:
        if link.find('a') is not None:
            print(link.find('a')['href'])
            count += 1

print('总数量：', count)



# 流程：
# 1. 读取 dists.txt 中所有网址
# 2. 分别提取各地区所有医院链接
# 3. 将这些医院链接入库

import requests
from bs4 import BeautifulSoup
import time
import pymysql

file = open('dists.txt', 'r')
dist_links = file.read().split('\n')

print(len(dist_links))
print(dist_links)

header={
    'user-agent': 'Mozzila/5.0'
}

# 数据库信息
host = 'localhost'
port = 3306
username = 'root'
password = 'root'
db = 'cola'
charset = 'utf8'

conn = pymysql.connect(host=host,
                       port=port,
                       user=username,
                       password=password,
                       db=db,
                       charset=charset,
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
insert_sql = r'insert into hosplinks(link, ifcrawed, hospname)'\
    + 'values(%s, %s, %s)'

count = 1
for dist_link in dist_links[:-1]:
    html_cont = requests.get(dist_link, headers=header, timeout=20).text.strip()
    soup = BeautifulSoup(html_cont, "html.parser")
    divs = soup.find_all('div', class_='tablist')
    for div in divs:
        links = div.find_all('li')
        for link in links:
            if link.find('a') is not None:
                lnk = link.find('a')['href']
                hospname = link.find('a').text.strip()
                dat = [lnk, 0, hospname]
                cursor.execute(insert_sql, dat)
                # print('****' + hospname + ': ' + lnk)
                count += 1
        conn.commit()
    time.sleep(3)

print('#####################################')
print('总数量：', count)
print('#####################################')

# 尝试下载某医院页面，提取其中信息

from urllib import request
import bs4

url = 'http://yyk.99.com.cn/'
resp = request.urlopen(url)
print(resp.getcode())
print(resp.read())

#print()



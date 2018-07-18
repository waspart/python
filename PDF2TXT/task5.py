# http.client 调用数据接口基本操作
# 百度翻译接口

import http.client
import hashlib
from urllib import parse
import random

appid = '20180408000143905'
key = 'E2BPaIOOYF49NMKQuNWH'

httpClient = None
url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
q = '中华人民共和国'
fromLang = 'zh'
toLang = 'en'
salt = random.randint(32768, 65536)
sign = appid + q + str(salt) + key
m1 = hashlib.md5()
m1.update(sign.encode(encoding='utf-8'))

sign = m1.hexdigest()
url = url + 'q=' + parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + \
      '&appid=' + appid + '&salt=' + repr(salt) + '&sign=' + sign
print(url)

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', url)
    response = httpClient.getresponse()
    s = response.read()
    print(s)
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
# print(s)

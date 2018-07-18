from urllib import request

url = 'http://www.whatismyip.com.tw/'

ip = '121.232.147.91:9000'
proxy = {
    'http': ip,
    'https': ip
}

proxy_support = request.ProxyHandler(proxy)
opener = request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')]
request.install_opener(opener)
response = request.urlopen(url)

html = response.read().decode('utf-8')
print(html)

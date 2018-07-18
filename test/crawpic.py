import requests
from bs4 import BeautifulSoup
import urllib.request

url = r'https://www.ruiwen.com/jiaocai/yuwen/renjiaoban/yinianjishangce/shangce3.html'
r = requests.get(url, timeout=20)

soup = BeautifulSoup(r.text, 'html.parser')
imgurl = 'https:' + soup.find('div', class_='pic').find('img')['src']
print(imgurl)

# b = urllib.request.urlopen(imgurl)
b = requests.get(imgurl, timeout=20)
f = open('img.jpg', 'wb')
# f.write(b.read())
f.write(b.content)
f.flush()
f.close()

print("Done!!!!!!!!")


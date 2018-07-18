import requests
from bs4 import BeautifulSoup
import lxml


url = "http://zd.hwxnet.com/pinyin.html"
cont = requests.get(url)
soup = BeautifulSoup(cont.text, 'lxml')
lst_py = soup.find_all("a", class_="pinyin_sub_idx")
# print(lst_py)
# print(len(lst_py))
for item in lst_py:
    print(item["href"])
    with open("py.txt", "a+") as fw:
        fw.write(item["href"] + "\n")





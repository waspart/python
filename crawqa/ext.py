import requests
from bs4 import BeautifulSoup

head = {
	'user-agent': 'Mozail/5.0'
}
url = r'http://jbk.39.net/sz/150507/4620753.html'
# html_cont = requests.get(r'http://jbk.39.net/sz/150507/4620753.html', headers=head)
html_cont = requests.get(url, headers=head)
print(html_cont.encoding)
html_cont.encoding = 'utf-8'
soup = BeautifulSoup(html_cont.content, 'html.parser')

main_cont = soup.find('div', class_='art_box')
# print(main_cont.text)

# print(len(lst_item))
# for itm in lst_item:
# 	print(itm)

title_h1 = main_cont.find('h1').text
print("问题为：  {}".format(title_h1))

summary = main_cont.find('p', class_='summary').text
print("核心提示：   {}".format(summary))

art_cont = main_cont.find('div', class_='art_con')
lst_p = art_cont.find_all('p')
print("答案原文：", end="  ")
for p in lst_p:
	# print(p.text.encode('iso-8859-1').decode('gb2312'))
	print(p.text)

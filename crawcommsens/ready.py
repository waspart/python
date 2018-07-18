import requests
from bs4 import BeautifulSoup, element
import bs4

url = r'http://www.360changshi.com/jk/jiankang/739725.html'
head={
    'user-agent': 'Mozila/5.0'
}
res = requests.get(url, headers=head)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    summary = soup.find('div', class_='summary').text
    # print('导语：{}'.format(summary.encode('iso-8859-1').decode('utf-8')))
    desc = soup.find('div', class_='desc')
    # print(str(soup.p.string).encode('iso-8859-1').decode('utf-8'))
    # for child in desc.descendants:
    #   print(type(child))
    #   if isinstance(child, bs4.element.NavigableString):
    #       print(str(child.string))
    #   else:
    #       print(child.text.encode('iso-8859-1').decode('utf-8'))
    # h3 = desc.find('h3')
    # print(h3.name)
    # print(h3.text.encode('iso-8859-1').decode('utf-8'))
    # print(h3.find_next_sibling().text.encode('iso-8859-1').decode('utf-8'))
    # try:
    #     ps = desc.children
    #     for p in ps:
    #         print(str(p).encode('latin-1', 'replace').decode('utf-8'))
    #         print()
    #         # print(p.text.strip().encode('latin-1', 'replace').decode('utf-8'))
    # except:
    #     print('出现编码错误')
    # finally:
    #     print('end')

    ps = desc.find_all('p')
    for p in ps:
        print(p.text.strip().encode('latin-1', 'replace').decode('utf-8'))
        print()
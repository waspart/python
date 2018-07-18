import requests
from bs4 import BeautifulSoup

url = 'http://cd.hwxnet.com/view/iieaoahbegphpndl.html'
head = {'user-agent': 'Mozila/5.0'}

res = requests.get(url, headers=head, timeout=10)
soup = BeautifulSoup(res.text, 'html.parser')

cy = soup.find('div', class_='view_title').find('span', class_='dullred f24 ff_yh m_r20').text
py = soup.find('div', class_='view_title').find('span', class_='pinyin f20').text
ju = soup.find('div', class_='view_con clearfix').find('p').text

print('词语：{}'.format(cy))
print('拼音：{}'.format(py))
print('解释：{}'.format(ju))



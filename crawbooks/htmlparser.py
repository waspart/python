from bs4 import BeautifulSoup
import requests

class HtmlParser(object):

	def getImg(self, url):
		return requests.get(url).content
		
	def parse(self, html_cont):
		soup = BeautifulSoup(html_cont, 'html.parser')
		img_url = 'https:' + soup.find('div', class_='pic').find('img')['src']
		new_url = 'https://www.ruiwen.com' + soup.find('div', class_='paging').find('a', class_='two')['href']
		return img_url, new_url





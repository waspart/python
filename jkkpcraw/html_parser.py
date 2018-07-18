from bs4 import BeautifulSoup

class HtmlParser(object):
	
	def parse(self, html_cont):
		result = []
		if html_cont is None:
			return None
		soup = BeautifulSoup(html_cont, 'html.parser')
		main_cont = soup.find('div', class_='article_l mt_20 mb_20')
		title = main_cont.find('div', class_='bk_qwkp_bt').text
		result.append(title)

		createDate = main_cont.find('div', class_='bk_qwkp_xqin_l fl').find('span').text
		result.append(createDate)

		artcont = ''
		artcont_lst = main_cont.find('div', class_='bk_qwkp_wzrr').find_all('p')
		for con in artcont_lst:
			artcont += con.text
		result.append(artcont)

		return result
		
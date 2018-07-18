from bs4 import BeautifulSoup

class Parser(object):
	"""docstring for Parser"""
	# def __init__(self, arg):
	# 	# super(Parser, self).__init__()
	# 	self.arg = arg

	def parse(self, html_cont, cyid):
		results = []
		if html_cont is None or html_cont.strip() == '':
			return None

		cy = ''
		py = ''
		ju = ''

		soup = BeautifulSoup(html_cont, 'html.parser')
		title = soup.find('div', class_='view_title')
		if title is not None:
			cy = title.find('span', class_='dullred f24 ff_yh m_r20').text
			py = title.find('span', class_='pinyin f20').text
			
		con = soup.find('div', class_='view_con clearfix')
		if con is not None:
			ju = con.find('p').text

		results.append(cy)
		results.append(py)
		results.append(ju)
		results.append(cyid)

		return results



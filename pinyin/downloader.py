import requests

class Downloader(object):
	head = {'user-agent': 'Mozila/5.0'}
	def download(self, url):
		try:
			res = requests.get(url, headers=self.head, timeout=30)
			if res.status == 200:
				return res.text
			else:
				return None
		except:
			print('获取网页内容出错（超时或其他）！', end="  ")
			return None
		# finally:
		# 	return 

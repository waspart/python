import requests

class HtmlDownloader(object):
	
	def download(self, url):
		if url is None:
			return None

		head = {'user-agent': 'myapp/1.0'}
		try:
			res = requests.get(url, headers=head, timeout=30)
			if res.status_code == 200:
				return res.text
			else:
				return None
		except:
			return None

		#print(res.read())

		# return res.text

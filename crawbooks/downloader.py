import requests

class Downloader(object):
	
	def download(self, url):
		head = {
		    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
		}
		req = requests.get(url, timeout=20, headers=head)
		if req.status_code == 200:
			return req.text
		else:
			return -1
		
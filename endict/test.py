from downloader import Downloader
import requests


# dloader = Downloader()
url = "https://www.merriam-webster.com/browse/dictionary/a"
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
try:
	text = requests.get(url, headers=headers, timeout=90).text
except:
	print("出现异常")
print(text)


import requests


class Downloader(object):

    header = {'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch, br',
              'Accept-Language': 'zh-CN,zh;q=0.8', }

    def download(self, url):
        try:
            res = requests.get(url, headers=self.header, timeout=60)
            if res.status_code == 200:
                return res.text
            else:
                return None
        except:
            print("下载网页出现错误！")
            return None

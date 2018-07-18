import requests


head = {'user-agent':'Mozilla/5.0'}
class Downloader(object):
    def download(self, url):
        # print(url)
        try:
            res = requests.get(url)
            if res.status == 200:
                return res.text
            else:
                return None
        except:
            print('获取网页内容出错（超时或其他）！', end="  ")
            return None
        # finally:
        #   return 
from downloader import Downloader
from paser import Parser


if __name__ == '__main__':
    dloader = Downloader()
    url = "http://zd.hwxnet.com/pinyin/a.html"
    # print(dloader.download(url))
    html_cont = dloader.download(url)

    pser = Parser()
    results = pser.parseDiv(html_cont)
    for item in results:
        print(item)

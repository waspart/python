# 爬虫主程序入口

import time
import url_manager, html_downloader, html_parser, html_outputer


class Spider(object):
    """docstring for Spider"""

    def __init__(self):
        super(Spider, self).__init__()
        self.urlmanager = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        print('init successfully!!!!!!!!!!!')

    def craw(self, root_url):
        count = 1
        self.urlmanager.add_new_url(root_url)
        while self.urlmanager.has_new_url():
            try:
                new_url = self.urlmanager.get_new_url()
                print('crawing', repr(count), ':', new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urlmanager.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break
                count += 1
            except:
                print('craw failed!')
            finally:
                print('Done!!!!!!!')
                self.outputer.output()


if __name__ == '__main__':
    root_url = r'http://yyk.99.com.cn/'
    spider_obj = Spider()
    spider_obj.craw(root_url)

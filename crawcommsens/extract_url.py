import requests
from bs4 import BeautifulSoup
import time
import random
import sqlproc, html_downloader
from multiprocessing import Process, Queue

class ExtractUrl(object):

    # host = 'localhost'
    host = '115.159.193.122'
    port = 3306
    username = 'root'
    # password = 'root'
    password = 'hkxx@206'
    db = 'cola'
    charset = 'utf8'
    root_url = r'http://www.360changshi.com/'
    # insert_sql = 'insert into linkstat(link, ifcrawed) values(%s, %s)'
    # head={'user-agent': 'Mozila/5.0'}


    def __init__(self):
        # super(ClassName, self).__init__()
        self.sqlsp = sqlproc.SqlProc(self.host, self.port, self.username, 
            self.password, self.db, self.charset)
        self.downloader = html_downloader.HtmlDownloader()

    def parse(self, html_cont):
        level2_urls = set()
        new_urls = set()
        soup_2 = BeautifulSoup(html_cont, 'html.parser')

        # 目标链接
        lists = soup_2.find_all('div', class_='list')
        if len(lists) > 0:
            for l in lists:
                new_urls.add(l.find('h3').find('a')['href'])
        # print(len(new_urls))
        
        # 2级链接
        paging = soup_2.find('div', class_='paging')
        spans = paging.find_all('span')
        if len(spans) > 0:
            for sp in spans:
                if sp.find('a') is not None:
                    level2_urls.add(self.root_url + sp.find('a')['href'])

        return new_urls, level2_urls

    def craw(self, que):
        res = self.downloader.download(self.root_url)
        if res is None:
            print('出现错误，超时或无法连接。。。。。。')
        soup = BeautifulSoup(res, 'html.parser')
        uls = soup.find('div', class_='leveltwo-list-content').find_all('ul') 
        for ul in uls[:-1]: 
            lis = ul.find_all('li')
            for li in lis:
                url = li.find('a')['href']
                print('#############################################')
                print('标题：{}, 链接：{}'.format(li.find('a').text.encode('iso-8859-1').decode('utf-8'), url))
                print('#############################################')

                set_level2_urls = set()
                set_level2_urls_done = set()
                set_level2_urls.add(url)

                while len(set_level2_urls) != 0:
                
                    this_url = set_level2_urls.pop()
                    set_level2_urls_done.add(this_url)

                    res_2 = self.downloader.download(this_url)
                    if res_2 is None:
                        print('连接 {} 出现错误，超时或无法连接!直接跳过'.format(this_url))
                        continue

                    new_urls, level2_urls = self.parse(res_2)
                    for uri in new_urls:
                        que.put(uri)
                    for uri in level2_urls:
                        if uri not in set_level2_urls_done and uri not in set_level2_urls:
                            set_level2_urls.add(uri)
                                        
                    time.sleep(abs(random.random() - 0.2))

    def inse(self, que):
        scount = 0
        insert_sql = 'insert into linkstat(link, ifcrawed) values(%s, %s)'
        while True:
            uri = que.get(True)
            bs, code = self.sqlsp.insertData(insert_sql, (uri, 0))
            if bs:
                scount += 1

            if scount % 1000 == 0:
                print('###############################################')
                print('####  成功插入1000条数据，目前共{}条  ####'.format(scount))
                print('###############################################')


if __name__ == '__main__':
    ex = ExtractUrl()
    que = Queue()
    pcraw = Process(target=ex.craw, args=(que,))
    pinse1 = Process(target=ex.inse, args=(que,))
    pinse2 = Process(target=ex.inse, args=(que,))
    pinse3 = Process(target=ex.inse, args=(que,))

    pcraw.start()
    pinse1.start()
    pinse2.start()
    pinse3.start()

    pcraw.join()
    pinse1.terminate()
    pinse2.terminate()
    pinse3.terminate()
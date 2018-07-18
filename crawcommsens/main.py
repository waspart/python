import html_downloader, html_parser
import sqlproc
import time, random
from multiprocessing import Process, Queue

class SpiderMain(object):
    """docstring for SpiderMain"""
    host = 'localhost'
    port = 3306
    username = 'root'
    password = 'root'
    db = 'cola'
    charset = 'utf8'
    select_sql = "select id, ifcrawed, link from linkstat limit %s, %s"
    update_sql = "update linkstat set ifcrawed = 1 where id = %s"
    insert_sql = "insert into commonsense(arttitle, summary, artcont) values(%s, %s, %s)"

    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.sp = sqlproc.SqlProc(self.host, self.port, self.username, 
            self.password, self.db, self.charset)

    def craw(self, que):

        n = 100
        totalcount = 10000000 #需要修改
        no_lst = list(range(0, totalcount, 100))
        no_lst.append(totalcount)
        
        for no in no_lst:
            if totalcount - no < 100:
                n = totalcount - no

            lst_link = self.sp.selectData(self.select_sql, (no, n))
            if lst_link == -1:
                '''查询失败，直接跳过'''
                continue

            for link in lst_link:
                print('crawing...... {}'.format(link), end="  ")
                uid = link['id']
                url = link['link']
                ifcrawed = link['ifcrawed']

                if ifcrawed == 1:
                    '''该链接已经爬取过，直接跳过'''
                    continue

                html_cont = self.downloader.download(url)
                if html_cont is None:
                    '''获取内容为空， 直接跳过'''
                    continue

                parse_result = self.parser.parse(html_cont)
                # que.put(parse_result)
                if parse_result is not None:
                    try:
                        que.put(parse_result)
                    except:
                        print('放入队列失败')
                else:
                    print('爬取失败！')
                time.sleep(abs(random.random() - 0.2))

    def insData(self, que):
        while True:
            in_data = que.get()
            bs, code = self.sp.insertData(self.insert_sql, in_data)
            if bs:
                print('插入成功！ 第 {} 条记录。'.format(code), end="  ")
                if self.sp.updateData(self.update_sql, uid):
                    print('更新成功， Done!')
                else:
                    print('更新失败， Undo!')
            else:
                print('插入失败！')
        

if __name__ == '__main__':
    spider = SpiderMain()
    que = Queue()
    pcraw = Process(target=spider.craw, args=(que,))
    pinse1 = Process(target=spider.insData, args=(que,))
    pinse2 = Process(target=spider.insData, args=(que,))
    pinse3 = Process(target=spider.insData, args=(que,))

    pcraw.start()
    # time.sleep(60)
    pinse1.start()
    time.sleep(60)
    pinse2.start()
    time.sleep(60)
    pinse3.start()
    # 等待pcraw进程结束
    pcraw.join()
    # 强制关闭死循环
    pinse.terminate()
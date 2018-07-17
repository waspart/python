import time
from paser import Parser
from downloader import Downloader
from sqlproc import SqlProc


class SpiderMain(object):

    host = '115.159.193.122'
    port = 3306
    username = 'root'
    password = 'hkxx@206'
    db = 'cola'
    charset = 'utf8'
    insert_sql = "INSERT INTO hjzi(`character`, pyyb, kind, biuy, jbuy, xxuy) VALUES(%s, %s, %s, %s, %s, %s)"

    def __init__(self):
        self.dloader = Downloader()
        self.pser = Parser()
        self.sp = SqlProc(self.host, self.port, self.username,
                          self.password, self.db, self.charset)
        print("Main Spider is initialized successfully!")

    def getCh(self, url):
        html_cont = self.dloader.download(url)
        lst_intro = self.pser.parseDiv(html_cont)

        for intro in lst_intro:
            lst_in = intro.split("#")
            ch_url = lst_in[0]
            character = lst_in[2]
            pyyb = lst_in[1]
            print("链接：{}\t汉字：{}\t拼音：{}".format(ch_url, character, pyyb), end="\t")

            ch_cont = self.dloader.download(ch_url)
            # print(ch_cont)
            kind, biuy, jbuy, xxuy = self.pser.parseDict(ch_cont)
            # print((character, pyyb, kind, biuy, jbuy, xxuy), end="\t")

            self.sp.insertData(self.insert_sql, (character,
                                                 pyyb, kind, biuy, jbuy, xxuy))
            time.sleep(3)
            print("Done!!!!!")
            

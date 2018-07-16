import time
from paser import Parser
from downloader import Downloader
from sqlproc import SqlProc


class SpiderMain(object):
    
    host = 'localhost'
    port = 3306
    username = 'root'
    password = 'root'
    db = 'cola'
    charset = 'utf8'

    def __init__(self):
        self.dloader = Downloader()
        self.pser = Parser()
        self.sp = SqlProc(self.host, self.port, self.username, self.password, self.db, self.charset)
        print("Main Spider is initialized successfully!")

    def getCh(self):
        pass
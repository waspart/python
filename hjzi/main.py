from downloader import Downloader
from paser import Parser
from spiderMain import SpiderMain


if __name__ == '__main__':
    
    spider = SpiderMain()
    with open("py.txt", "r") as fw:
        while True:
            line = fw.readline().split("\n")[0]
            spider.getCh(line)
            if len(line.strip()) <= 0:
                break
            # print(line)

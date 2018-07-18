import downloader
import parser
import sqlproc
import random
import time
from multiprocessing import Process, Queue, Pool


class MainSpider(object):

	host = 'localhost'
	port = 3306
	username = 'root'
	password = 'root'
	db = 'cola'
	charset = 'utf8'

	def __init__(self):
		# super(MainSpider, self).__init__()
		self.dloader = downloader.Downloader()
		self.pser = parser.Parser()
		self.sp = sqlproc.SqlProc(self.host, self.port, self.username, 
            self.password, self.db, self.charset)
		print('MainSpider is initialized successfully !!!')

	def craw(self, que):
		n = 100
		totalcount = 381000 #需要修改
		no_lst = list(range(0, totalcount, 100))
        # no_lst.append(totalcount)
		select_sql = 'select id, link, ifcrawed from cylinkstat limit %s, %s'
        # update_sql = 'update cylinkstat set ifcrawed = 1 where id = %s'

		for no in no_lst:
			if totalcount - no < n:
				n = totalcount - no

			cylinks = self.sp.selectData(select_sql, (no, n))
			for cylink in cylinks:

				cyid = cylink['id']
				cyurl = cylink['link']
				ifcrawed = cylink['ifcrawed']
				
				res = self.dloader.download(cylink)
				if res is not None:
					parse_result = self.pser.parse(res, cyid)
					try:
						que.put(parse_result)
					except:
						print('放入队列失败！')

				time.sleep(abs(random.random() - 0.4))

	def inse(self, que, no):
		insert_sql = 'insert into ciyu(word, pinyin, uiyi) values(%s, %s, %s)'
		update_sql = 'update cylinkstat set ifcrawed = 1 where id = %s'
		while True:
			in_data = que.get(True)
			bs, code = self.sp.insertData(insert_sql, in_data[:3])
			if bs:
				print('进程{}\t入库成功！\t第 {} 条数据！'.format(no, code), end="  ")
				if self.sp.updateData(update_sql, (in_data[3])):
					print('更新成功！  Done！！！！')
				else:
					print('更新失败！  Undo！！！！')
			else:
				print('入库失败！')


if __name__ == '__main__':
	
	ms = MainSpider()
	que = Queue()

	pcraw = Process(target=ms.craw, args=(que,))
	pins1 = Process(target=ms.inse, args=(que, 1))
	pins2 = Process(target=ms.inse, args=(que, 2))
	# pins3 = Process(target=ms.inse, args=(que, 3))
	# pins4 = Process(target=ms.inse, args=(que, 4))
	# pins5 = Process(target=ms.inse, args=(que, 5))

	pcraw.start()
	pins1.start()
	pins2.start()
	# pins3.start()
	# pins4.start()
	# pins5.start()
	
	pcraw.join()

	pins1.terminate()
	pins2.terminate()
	# pins3.terminate()
	# pins4.terminate()
	# pins5.terminate()

	print('ALL DONE!!!!!!!')

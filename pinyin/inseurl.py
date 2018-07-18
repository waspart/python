import sqlproc
import time, random
from multiprocessing import Process, Queue

class InsertUrl(object):
	"""docstring for InsertUrl"""
	host = 'localhost'
    port = 3306
    username = 'root'
    password = 'root'
    db = 'cola'
    charset = 'utf8'

	def __init__(self):
		# super(InsertUrl, self).__init__()
		self.sp = sqlproc.SqlProc(self.host, self.port, self.username, 
            self.password, self.db, self.charset)

	def readUrl(self, que):
		with open('cylinks.py', 'r') as fin:
		u = fin.read()
		urls = u.split('*')[:-1]
		for url in urls:
			que.put(url)

	def inUrl(self, que):
		insert_sql = 'insert into cylinkstat(link, ifcrawed) values(%s, %s)'
		# url = que.get(True)
		while True:
			url = que.get(True)
			bs, code = self.sp.insertData(insert_sql, (url, 0))
			if bs:
				print('入库成功！\t第 {} 条数据！'.format(code))
			else:
				print('入库失败！')
		
if __name__ == '__main__':
	isn = InsertUrl()
	que = Queue()

	pread = Process(target=isn.readUrl, args=(que,))
	pins1 = Process(target=isn.inUrl, args=(que,))
	pins2 = Process(target=isn.inUrl, args=(que,))

	pread.start()
	pins1.start()
	pins2.start()

	pins1.terminate()
	pins2.terminate()


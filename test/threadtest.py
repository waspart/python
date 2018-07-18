import threading
import time

exitFlag = 0

class myThread(threading.Thread):
	"""docstring for myThread"""
	def __init__(self, threadID, name, delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.delay = delay

	def print_time(self, threadName, delay, counter):
		while counter:
			if exitFlag:
				threadName.exit()
			time.sleep(delay)
			print(threadName, ': ', time.ctime(time.time()))
			counter -= 1

	def run(self):
		print('开始线程：' + self.name)
		# threadLock.acquire()
		self.print_time(self.name, self.delay, 5)
		# threadLock.release()
		print('退出线程：' + self.name)
		

threadLock = threading.Lock()
threads = []

thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
	t.join()
	
print('退出主线程！')

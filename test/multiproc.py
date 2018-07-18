from multiprocessing import Process, Queue, Pool
import os, time

def write(q):
	print('我是 {}，开始存放队列'.format(os.getpid()))
	for i in list(range(100)):
		q.put(i)
		time.sleep(0.2)
	print('我是 {}，存放结束！！'.format(os.getpid()))


def read(q, name):
	print('我是 {} / {}，开始读取队列'.format(name, os.getpid()))
	while True:
		number = q.get(True)
		print('{}, 此次读取 {}'.format(name, number))

if __name__ == '__main__':
	
	q = Queue()
	pw = Process(target=write, args=(q,))

	p = Pool(4)
	for i in list(range(4)):
		p.apply_async(read, args=(q, 'proc' + repr(i), ))

	print('Start!!!!!!')
	pw.start()
	p.close()
	p.join()
	pw.join()

	print('DONE!!!!!!')

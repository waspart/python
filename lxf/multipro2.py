from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in list(range(100)):
        # print('Put %s to queue...' % value)
        q.put(value, block=False)
        time.sleep(random.random() + 1)

# 读数据进程执行的代码:
def read(q, name):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()
        print('%s Get %s from queue.' % (name, value))

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr1 = Process(target=read, args=(q, 'r1'))
    pr2 = Process(target=read, args=(q, 'r2'))
    pr3 = Process(target=read, args=(q, 'r3'))

    # 启动子进程pw，写入:
    pw.start()
    # time.sleep(1)
    # 启动子进程pr，读取:
    pr1.start()
    # time.sleep(1)
    pr2.start()
    # time.sleep(1)
    pr3.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr1.terminate()
    pr2.terminate()
    pr3.terminate()
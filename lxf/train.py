import asyncio
import threading
import time
import random
import types

@types.coroutine
def pr(s, num):
	print(s)
	# time.sleep(num)
	# asyncio.sleep(num)
	yield

# @asyncio.coroutine
async def pause(num):
	print("I am sleeping......  {}".format(threading.currentThread()))
	# yield from asyncio.sleep(num)
	# yield from pr('I am thread {}'.format(threading.currentThread()))
	# time.sleep(num)
	# await pr('I am thread {}'.format(threading.currentThread()), num)
	await asyncio.sleep(num)
	print("after {} secondes, I am full......  {}".format(num, threading.currentThread()))

if __name__ == '__main__':
	start = time.time()
	loop = asyncio.get_event_loop()
	tasks=[pause(random.randrange(10)), pause(random.randrange(10)), pause(random.randrange(10))]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()
	print('Time eclispe: {}'.format(time.time() - start))

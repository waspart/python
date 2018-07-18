import threading
import asyncio
import time

# @asyncio.coroutine
async def printMsg():
	print('中场休息')
	time.sleep(1)
	return []

# @asyncio.coroutine
async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # yield from printMsg()
    await asyncio.sleep(1)
    print('hello')
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
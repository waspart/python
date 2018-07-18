import asyncio
import time

now = lambda : time.time()

async def do_something(x):
	print('waiting: ', x)
	# time.sleep(2)
	await asyncio.sleep(x)
	return 'Done after {}s'.format(x)

def callback(future):
	print('callback: {}'.format(future.result()))

# start = now()
# cor = do_something(2)
# loop = asyncio.get_event_loop()
# task = loop.create_task(cor)
# task = asyncio.ensure_future(cor)
# task.add_done_callback(callback)
# print(task)
# tasks = [
# 	asyncio.ensure_future(do_something(2)),
# 	asyncio.ensure_future(do_something(5)),
# 	asyncio.ensure_future(do_something(4))
# ]
# for t in tasks:
# 	t.add_done_callback(callback)
# loop.run_until_complete(asyncio.wait(tasks))
# # print(task)
# for t in tasks:
# 	print('task ret: '.format(t.result()))
# print('Time:{}'.format(now() - start))
async def main():
    coroutine1 = do_something(1)
    coroutine2 = do_something(2)
    coroutine3 = do_something(4)
 
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
 
    dones, pendings = await asyncio.wait(tasks)
 
    for task in dones:
        print('Task ret: ', task.result())
 
start = now()
 
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
 
print('TIME: ', now() - start)
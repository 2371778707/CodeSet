import asyncio

import time

now = lambda: time.time()


async def do_some_work(x,y):
    print('Waiting: ', x,y)

    await asyncio.sleep(x)
    return x,y


async def main():
    coroutine1 = do_some_work(1,'a')
    coroutine2 = do_some_work(1,'b')
    coroutine3 = do_some_work(1,'c')

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    dones = await asyncio.gather(*tasks)
    for task in dones:
        print('Task ret: ', task)


start = now()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print('TIME: ', now() - start)
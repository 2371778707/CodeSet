import asyncio
from aiohttp import ClientSession
from concurrent.futures import ProcessPoolExecutor

async def fetch(i,url):
    async with ClientSession() as session:
        async with session.get(url, verify_ssl=False) as response:
            a = await response.read()
            print(a)
            return i


async def bound_fetch(i,sem,url):
    # getter function with semaphore
    async with sem:
        await fetch(i,url)


async def run( r):
    url = "http://www.firefoxchina.cn/"
    tasks = []
    sem = asyncio.Semaphore(1000)
    for i in range(r):
        task = asyncio.ensure_future(fetch(i,url))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)
    return responses

async def ti(n):
    asyncio.sleep(1)
    return n+1
def a(l,ti):

pool = ProcessPoolExecutor()
async def tii(pool,func,n):
    return asyncio.get_event_loop().run_in_executor(pool,a)
from functools import wraps
import time
def timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        r = await func(*args,**kwargs)
        end = time.time()
        print(f"cost:{end-start}s")
        return r
    return wrapper
@timer
async def add():
    list = await run(2000)
    for i in list:
        c = await ti(i)
        print(c)
@timer
async def add1():
    r = await run(2000)
    tasks = [asyncio.ensure_future(tii(pool,ti,i)) for i in r]
    r =  await asyncio.gather(*tasks)
    print(r)
a = asyncio.get_event_loop()
a.run_until_complete(add1())

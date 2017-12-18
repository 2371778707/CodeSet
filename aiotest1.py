#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
import asyncio
import aiohttp
async def run1(r):
    async with aiohttp.ClientSession() as sess:
        async with sess.get("https://www.baidu.com", verify_ssl=False) as res:
            r =res.status
            print(r)
            return r
async def add(r):
    for i in range(r):
        rr = await run1(i)
        for i in range(rr):
            rr += i
            print(rr)
loop = asyncio.get_event_loop()
loop.run_until_complete(add(10000))
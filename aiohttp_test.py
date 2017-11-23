# !/usr/bin/env python
#-*-coding:utf-8-*-


import aiohttp
import asyncio
params = [('key', 'value1'), ('key', 'value2')]
headers = {'content-type': 'application/json'}
conn = aiohttp.TCPConnector()
async def fetch(client):
    async with client.get('http://www.baidu.com',
                          params=params,
                          headers=headers
                          ) as resp:
        assert resp.status == 200
        print(resp.status)
        # return await resp.text()


async def main():
    async with aiohttp.ClientSession(connector=conn) as client:
        html = await fetch(client)
        print(html)

"""
想要通过这个框架来异步发送请求，可以是下面这样
"""


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
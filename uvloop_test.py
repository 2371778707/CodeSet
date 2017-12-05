import uvloop
import asyncio

l =uvloop.EventLoopPolicy()
asyncio.set_event_loop_policy(l)
a = asyncio.get_event_loop()
print(a)
#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
import time
from concurrent.futures import ThreadPoolExecutor
import threading

# 可回调的task
def pub_task(msg):
    time.sleep(1)
    print(threading.current_thread())
    return msg

# 创建一个线程池
pool = ThreadPoolExecutor(max_workers=3)

# 往线程池加入2个task
task1 = pool.submit(pub_task, 'a')
task2 = pool.submit(pub_task, 'b')

print(task1.done())        # False
time.sleep(4)
print(task2.done())        # True

print(task1.result())
print(task2.result())
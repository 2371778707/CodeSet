#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="实现python优先级队列的几种方式"
print(globals())
#1 使用list来实现 插入时间为o(n2)
a = []
a.append((1,"a"))
a.append((11,"aa"))
a.sort(reverse=True)
# print(a)
# while a:
#     aa = a.pop()
#     print(aa)

#2 使用heapq最小堆来实现 插入时间为o(nlogn)
import heapq
b = []
heapq.heappush(b,(222,"aaa"))
heapq.heappush(b,(2,"a"))
heapq.heappush(b,(22,"aa"))
# print(b)
# while b:
#     bb = heapq.heappop(b)
#     print(bb)

#3 使用queue队列的priorityqueue 内部使用heapq来实现，因此插入时间相同
from queue import PriorityQueue

c = PriorityQueue()
c.put((22,"aa"))
c.put((2,"a"))
c.put((222,"aaa"))
# print(c)
# while not c.empty():
#     cc = c.get()
#     print(cc)

#4 另外的几种队列形式
from queue import Queue
#先入先出的队列
from queue import LifoQueue
#后进先出的队列
from collections import deque
#双端队列
print(globals())

from queue import  PriorityQueue
import threading


class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return

    def __lt__(self, other):
        return (self.priority<other.priority)


q = PriorityQueue()
q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))


def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()


workers = [threading.Thread(target=process_job, args=(q,)),
           threading.Thread(target=process_job, args=(q,)), ]
for w in workers:
    w.setDaemon(True)
    w.start()
q.join()

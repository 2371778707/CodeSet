#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
import multiprocessing
c = 0
l = multiprocessing.Lock()
from multiprocessing import Process
class A(Process):
    def __init__(self):
        super(A,self).__init__()
    def run(self):
        global c,l
        if l.acquire():
            c +=1
            print("进程加一",self.name,c)
            l.release()
for i in range(10):
    a = A()
    a.start()
    a.join()
print(c)
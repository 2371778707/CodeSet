#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="pipe的两个进程通信，分别是单双工，全双工"

import multiprocessing
import random
import os,time
def proc_send(pipe,urls):
    for i in urls:
        print("Process-{},send:{}".format(os.getpid(),i))
        pipe.send(i)
        time.sleep(3)
        print(pipe.recv())
def proc_recv(pipe):
    while True:
        print("Process-{},recv:{}".format(os.getpid(),pipe.recv()))
        time.sleep(3)
        pipe.send("ok")
pipe = multiprocessing.Pipe()
print(pipe)
p1 = multiprocessing.Process(target=proc_send,args=(pipe[0],['url_'+str(i) for i in range(3)]))
p2 = multiprocessing.Process(target=proc_recv,args=(pipe[1],))
p1.start()
p2.start()
p1.join()
p2.join()
#-*-coding:utf-8-*-
#多线程操作
import threading
from queue import Queue
class a(threading.Thread):
    def __init__(self,q):
        super(a,self).__init__()
        self.q = q
    def run(self):
        print(threading.Thread.getName(self))
        while True:
            a=0
            if self.q.empty():
                self.q.put(a)
                a+=1
                print("装填:",a)
class b(threading.Thread):
    def __init__(self,q):
        super(b,self).__init__()
        self.q = q
    def run(self):
        print(threading.Thread.getName(self))
        while True:
            if not self.q.empty():
                a = self.q.get()
                print("获取到:",a)
if __name__=="__main__":
    q = Queue()
    a,b = a(q),b(q)
    a.start()
    b.start()
    a.join()
    b.join()
    a.close()

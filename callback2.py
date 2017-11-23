#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="回调的演示"

class CallbackBase:
    def __init__(self):
        self._callback = {}
        for k in (getattr(self,x)for x in dir(self)):
            if hasattr(k,"one"):
                self._callback.setdefault(k.one,[]).append(k)
            elif hasattr(k,"list"):
                for j in k.list:
                    self._callback.setdefault(j,[]).append(k)
    @staticmethod
    def callback(e):
        def f(g,ev=e):
            g.one = ev
            return g
        return f
    @staticmethod
    def callbacklist(e):
        def f(g,ev=e):
            g.list=ev
            return g
        return f
    def dispath(self,event):
        l = self._callback[event]
        f = lambda *args,**kwargs:map(lambda x:x(*args,**kwargs),l)
        return f
class M(CallbackBase):
    e1 =1
    e2 =2
    @CallbackBase.callback(e1)
    def pr1(self,pa=None):
        print(pa)
        return None
    @CallbackBase.callbacklist([e1,e2])
    def pr2(self,pa=None):
        print(pa)
        return None
    def run(self,e,p):
        self.dispath(e)(p)
a = M()
a.run(M.e1,"a")
a.run(M.e2,"b")
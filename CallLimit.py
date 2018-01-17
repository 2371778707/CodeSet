#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
class A:
    def __init__(self):
        self.ac =1
    def a(self):
        print(self.ac)
class CallTimesLimit(object):
    def __init__(self, max):
        self.__max = max
        self.__count = 0
        self.cls = A()
    def __call__(self, fun):
        self.__fun = fun
        return self.__proxy

    def __proxy(self, *args, **kwargs):
        self.__count += 1
        if self.__count > self.__max:
            raise Exception("{f} is called over {limit} times".format(f=self.__fun.__name__,
                                                                      limit=self.__max))
        else:
            self.__fun(self.cls,*args, **kwargs)
class A:
    def __init__(self):
        self.ac =1
    @CallTimesLimit(2)
    def a(self):
        print(self.ac)

aa = A()
print()
for i in range(3):
    aa.a()

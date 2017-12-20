#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
class T(type):
    def __new__(meta,name,base,d):
        if base!=(object,):
            if d["a"]>3:
                raise ValueError
        return type.__new__(meta,name,base,d)
class A(metaclass=T):
    a=4
a = A()
class A:
    def
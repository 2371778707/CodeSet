#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
class T:
    def __init__(self):
        self.v *=2
    @staticmethod
    def a():
        pass
class P:
    def __init__(self):
        self.v+=5
    def b(self):
        pass
class aa(P,T):
    def __init__(self,v):
       self.v = v
       print(self.v)
       super(__class__,self).__init__()
       super(__class__,self).__init__()

       # super.__init__(self)
a  = aa(3)
from pprint import pprint
print(aa.a())

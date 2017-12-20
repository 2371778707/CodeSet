#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
class InputData:
    def read(self):
        raise NotImplementedError
a = InputData()
class P(InputData):
    def __init__(self,p):
        super(P,self).__init__()
        self.p = p
    def read(self):
        return open(self.p).read()
print(a.read())
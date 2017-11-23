# !/usr/bin/env python
#-*-coding:utf-8-*-
#自定义context
"""
as 后面接的变量，是由__enter__返回值决定的

"""
class gc():
    def __init__(self,str):
        self.str = str

    def __enter__(self):
        print("begin",self.str,"enter")
        a = self.str+"world"
        return a
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("end",str,"exit")
# with gc("hello") as c:
#     print(c)

#使用contextlib来构造上下文管理器
import contextlib
from contextlib import contextmanager
@contextmanager
def cc(str):
    print("begin",str)
    yield "here"
    print("end",str)
# with cc("lin") as c:
#     print(c)

#使用结合来管理多嵌套ctx
#未结合
with cc("lin") as lin:
    with cc("han") as han:
        with cc("qiu") as qiu:
            print(lin+han+qiu)
#结合
with cc("lin") as l,cc("han") as b,cc("qiu") as c:
    print(l,b,c)
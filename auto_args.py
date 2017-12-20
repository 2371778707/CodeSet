#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="用none和文档字符串来描述具有动态默认值参数"
import datetime
import time
def a(m, w = datetime.date()):
    print(m,w)
def a1(m,w = None):
    w = datetime.date()
    print(m,w)
a1("a")
time.sleep(1)
a1("b")


#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
# nonlocal 和global
"""
nonlocal 获取闭包数据，修改全局数据
global 获取数据，但不修改

"""
def a():
    a=1
    def aa():
        nonlocal a
        a=3
        return a
    c = aa()
    return a,c
c  = a()
print(c)
#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __datetime__
# __purpose__

from contextlib import contextmanager

@contextmanager
def test1(arg):
    print("no1 begin")
    yield arg+"1"
    print("no1 end")

@contextmanager
def test2(arg):
    print("no2 begin")
    yield arg+"2"
    print("no2 end")

with test1("task") as a,test2("task")as b:
    print(a,"\n",b)
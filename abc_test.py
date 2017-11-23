#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""

import abc
class abc2(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def foo(self):
        return "foo"
#必须重写foo方法
# a = abc()
# print(abc.foo)
class abc1(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def foo(cls):
        return 4
# a =abc1()
print(abc1.foo())
import functools
a = functools.partial(print,"a")
print(a)
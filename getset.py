#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
class Grade:
    def __init__(self):
        self.v = {}
    def __get__(self, instance, owner):
        if not instance:return self
        return self.v.get(instance,0)

    def __set__(self, instance, value):
        self.v[instance]=value
class Exam:
    a = Grade()
    b = Grade()
a = Exam()
b = Exam()
a.a=3
b.a=4

print(a.a,b.a)
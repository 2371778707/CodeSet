#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="切片操作"

class Slice:
    def __init__(self):
        self.item = [1,2,3,4,5]
    def __setitem__(self, key, value):
        self.item[key] = value

    def __getitem__(self, item):
        return self.item[item]
# 实例测试
a = Slice()
print(a[1])
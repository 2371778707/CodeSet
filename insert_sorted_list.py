#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="插入数据到已经排好序的列表"
from bisect import bisect,insort
a = [1,2,5,4,3]
a.sort()
insort(a,7)
print(bisect(a,2))
print(a)
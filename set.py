#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="求两个列表之间的不同"


def diff(l1,l2):
    """l2是l1的子集"""
    diff_ = set(l1) - set(l2)
    return diff_


l1 = [1,2,3]

l2 = [2,3,]

print(diff(l1,l2))
#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 013_tuple.py
@time: 2017/1/15 18:25
"""

tuple1 = (1, 2)
print(tuple1)
print(tuple1[0])

temp = (1)
print(type(temp)) # <class 'int'>
temp = (1, )
print(type(temp)) # <class 'tuple'>

print(8 * (8)) # 64
print(8 * (8, )) # (8, 8, 8, 8, 8, 8, 8, 8)

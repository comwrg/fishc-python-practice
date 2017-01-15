#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 011_array.py
@time: 2017/1/15 17:46
"""

arr = [0, 1, 2, 3, 4, 5]
# first method
arr.remove(0)
# second method
del arr[0]
# third method
arr = [0, 1, 2, 3, 4, 5]
n = arr.pop()
print(arr)
print(n)

arr = [0, 1, 2, 3, 4, 5]
print(arr[1:3]) # [1, 2]
print(arr[:3]) # [0, 1, 2]
print(arr[:]) # new copy

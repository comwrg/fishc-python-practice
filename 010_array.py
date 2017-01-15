#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 007_array.py
@time: 2017/1/15 11:46
"""

arr = [1, 2, 3, 4, 5]
print(arr) # [1, 2, 3, 4, 5]

arr.append(6)
print(arr) # [1, 2, 3, 4, 5, 6]

arr.extend([7, 8])
print(arr) # [1, 2, 3, 4, 5, 6, 7, 8]

arr.insert(0, 0)
print(arr) # [0, 1, 2, 3, 4, 5, 6, 7, 8]


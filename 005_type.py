#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 005_type.py
@time: 2017/1/14 23:13
"""

# e记法
e = 15e10
print(e) # 150000000000.0

# get type
i = 0
print(type(i)) # <class 'int'>
f = 0.1
print(type(f)) # <class 'float'>

# type is equal
s = 'fishc'
print(isinstance(s, str)) # True

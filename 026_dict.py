#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 026_dict.py
@time: 2017/2/4 13:21
"""

dict1 = {}
dict1 = dict1.fromkeys(range(3))
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(1 in dict1)
print(dict1.clear())

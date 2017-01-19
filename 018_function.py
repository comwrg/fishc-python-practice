#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 018_function.py
@time: 2017/1/19 13:21
"""

print(help(print))
def test(*params):
    for p in params:
        print(p)

test(1, 2, 3)

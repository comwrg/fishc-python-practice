#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 023_recursion.py
@time: 2017/2/3 13:41
"""


# 斐波那契数列
def f(n):
    if n < 3:
        return 1
    else:
        return f(n - 1) + f(n - 2)

print(f(12))

#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 022_recursion.py
@time: 2017/2/1 11:55
"""

def f(n):
    if(n == 1):
        return n
    print('%s * %s' % (n-1, n))
    return f(n - 1) * n

print(f(400))

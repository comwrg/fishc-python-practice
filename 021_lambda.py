#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 021_lambda.py
@time: 2017/2/1 12:29
"""

y = lambda x : x * x
print(y(2))

print(list(filter(None, [True, False, 1, 0])))

print(
    list(
        filter(
            lambda x: x % 2 == 0,
            range(0,10)
        )
    )
)

print(
    list(
        map(
            lambda x: x * x,
            range(1, 10)
        )
    )
)

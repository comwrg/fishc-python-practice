#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 024_hanoi.py
@time: 2017/2/3 14:22
"""

def hanoi(n, x='X', y='Y', z='Z'):
    ARROW = ' -> '

    if n == 1:
        print(x, ARROW, z)
    else:
        # 将前n-1个盘子从 x 上移动到 y 上
        hanoi(n-1, x, z, y)
        # 将前最后一个盘子从 x 移动到 z 上
        hanoi(1, x, y, z)
        # 将 y 上的盘子移动到 z 上
        hanoi(n-1, y, x, z)

hanoi(3)

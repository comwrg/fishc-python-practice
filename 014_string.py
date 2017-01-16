#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 014_string.py
@time: 2017/1/16 18:08
"""

str1 = 'I love fishc.com'
print(str1[:6]) # I love
print(str1[5]) # e
print(str1.capitalize()) # 首字母大写
print(str1.casefold()) # 全部小写
print(str1.center(40, ' ')) # 填充
print(str1.count('fi')) # 出现的次数
print(str1.endswith('com')) # 以什么为结尾
print(str1.find('I'))
print(str1.join('12'))

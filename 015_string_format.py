#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 015_string_format.py
@time: 2017/1/18 9:39
"""

print("{0} love {1}".format("I", "fishc.com"))
print("{a} love {b}".format(a='I', b='fishc.com'))
print("{{0}}".format())
print('{{0}}')
print('{0:.1f}{1}'.format(27.658, 'GB'))
print('%c' % 97)
print('%s' % 'I love fishc.com')
print('%d' % 6)
print('%f' % 1.2)
print('%e' % 10000.22)
print('%g' % 10000.22)
print('%010d' % 5)

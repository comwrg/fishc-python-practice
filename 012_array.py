#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: 012_array.py
@time: 2017/1/15 18:00
"""

list1 = [1]
list2 = [2]
print(list1 > list2) # false

list1 = [2, 4]
list2 = [2, 3]
print(list1 > list2) # true

list1 = [1, 2]
list2 = [1, 2]
print(list1 == list2) # true

list3 = list1 + list2
print(list3) # [1, 2, 1, 2]

list1 = [1, 2]
print(list1 * 2) # [1, 2, 1, 2]

print(1 in list1) # true

print(dir(list))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
list1 = [1, 2]
list1 *= 5
print(list1.count(1)) # 1 出现的次数
print(list1.index(1)) # 0
print(list1.index(1, 2)) # 2

list1 = [1, 2]
list1.reverse()
print(list1) # [2, 1]

list1 = [2, 1, 3]
list1.sort()
print(list1) # [1, 2, 3]

list1.sort(reverse=True)
print(list1) # [3, 2, 1]




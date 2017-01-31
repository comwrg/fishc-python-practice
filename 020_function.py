#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@time:   2017/01/31 12:49
"""


count = 5
def myFun():
    count = 10
    return count

print count
print myFun()


def fun1():
    print 'fun1 is running .'
    def fun2():
        print 'fun2 is running'
    fun2()
    return
fun1()

def funX(x):
    def funY(y):
        return x * y
    return funY

print funX(88888888)(1)
"""
# can be run in python 3
# because of keyword 'nonlocal'

def funA(a):
    x = 2
    def funB(b):
        nonlocal x *= x
        return x
    return funB()
funA()
"""

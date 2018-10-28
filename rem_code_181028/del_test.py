# -*- coding:utf-8 -*-
__date__ = '2018/10/28 11:47'

import sys

a = 100
b = a

del a

print(b)   #100
print(a)   #NameError: name 'a' is not defined


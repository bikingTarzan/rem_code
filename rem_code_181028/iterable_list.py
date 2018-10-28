# -*- coding:utf-8 -*-
__date__ = '2018/10/28 16:39'

from collections.abc import Iterable, Iterator

a = [1,2,3]

print(isinstance(a, Iterable))   #True
print(isinstance(a, Iterator))   #False
print(isinstance(iter(a), Iterator))  #True

print("__iter__"in dir(a))     #True,迭代协议，定义了的对象代表可迭代
print("__next__"in dir(a))     #False，

# -*- coding:utf-8 -*-
__date__ = '2018/10/21 16:44'

class A():
    def __init__(self, mem_list):
        self.mem_list = mem_list

    def __iter__(self):
        return iter(self.mem_list)

a = A(range(10))

print(type(a))

for v in a:
    print(v)


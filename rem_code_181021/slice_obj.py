# -*- coding:utf-8 -*-
__date__ = '2018/10/21 16:46'

import numbers

class A():
    def __init__(self, name, mem_list):
        self.name = name
        self.mem_list = mem_list

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(name=self.name, mem_list=self.mem_list[item])

        elif isinstance(item, numbers.Integral):
            return cls(name=self.name, mem_list=self.mem_list[item])


a = A("xiaoming", range(10))

print(list(a[:5].mem_list))

for v in a:
    print(v.__dict__)



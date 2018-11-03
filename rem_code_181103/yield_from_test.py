# -*- coding:utf-8 -*-
__date__ = '2018/11/3 10:19'


def run():
    yield from range(10)

a=run()

for i in a:
    print(i)


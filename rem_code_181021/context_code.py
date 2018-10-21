# -*- coding:utf-8 -*-
__date__ = '2018/10/21 15:05'

import contextlib

def run(obj):
    for i in obj:
        yield i
        # print(i)

@contextlib.contextmanager
def file_open(file):
    a = range(100)
    print("file open")
    yield a
    print("file end")



with file_open("bobby.txt") as f_open:
    print("file processing")
    for v in run(f_open):
        print(v)

#输出
# file open
# {}
# file end
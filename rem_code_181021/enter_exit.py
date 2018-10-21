# -*- coding:utf-8 -*-
__date__ = '2018/10/21 14:48'

import time

from multiprocessing import Process

class A:
    def __init__(self, t):
        print("init")
        self.time = t

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def __del__(self):
        print("del")

    def run(self):
        time.sleep(self.time)
        print("run")

# a = A()
# a.run()
# print("******************")
# with A() as b:
#     b.run()

def work(t):
    a_obj = A(t)
    a_obj.run()


a1 = Process(target=work, args=(5,))
a2 = Process(target=work, args=(10,))

a1.start()
a2.start()

a1.join()
a2.join()
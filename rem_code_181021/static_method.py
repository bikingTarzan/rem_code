# -*- coding:utf-8 -*-
__date__ = '2018/10/21 14:14'


class A():
    def __init__(self):
        pass

    @staticmethod
    def run():
        print("run")

    @classmethod
    def class_method(cls):
        return cls.run()

a = A()

# a.run()
# A.run()

a.class_method()
A.class_method()

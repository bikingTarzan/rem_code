# -*- coding:utf-8 -*-
__date__ = '2018/10/28 14:05'

class Person(type):
    def __new__(cls, *args, **kwargs):
        print("in person new")
        return super().__new__(cls, *args, **kwargs)

class Student(metaclass=Person):
    def __init__(self):
        pass

    def run(self):
        print("run")

s = Student()
s.run()


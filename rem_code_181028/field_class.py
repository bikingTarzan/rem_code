# -*- coding:utf-8 -*-
__date__ = '2018/10/28 12:38'

import numbers

class IntField:
    def __get__(self, instance, value):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value , numbers.Integral):
            raise ValueError("value need int")
        if value < 0:
            raise ValueError("value need > 0")
        self.value = value

    def __delete__(self, instance):
        pass

class NotDataField:
    def __get__(self, instance, value):
        return self.value


class Person:
    age = IntField()
    col = IntField()

if __name__ == "__main__":
    p1 = Person()
    p1.age = 10
    print(p1.age)
    p1.name = "xiaoming"
    print(p1.name)
    print(p1.__dict__)

    print("========== 1 ============")
    p2 = Person()
    print(p2.age)
    p2.age =30
    print(p2.age)
    print(p1.age)

    print("========== 2 ============")
    p1.col = 100
    p2.col = 200

    print(p1.col)
    print(p2.col)
    print(p1.__dict__)

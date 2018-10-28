# -*- coding:utf-8 -*-
__date__ = '2018/10/28 12:07'

from datetime import date, datetime

class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == "__main__":
    p = Person("xiaoming", date(year=1990, month=1, day=1))

    print(p.age)
    p.age = 30
    print(p._age)


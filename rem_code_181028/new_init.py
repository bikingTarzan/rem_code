# -*- coding:utf-8 -*-
__date__ = '2018/10/28 13:50'

class Person:
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        print("in init")

class Student(Person):
    def __init__(self,name):
        super().__init__(name)
        print("is student")
        print(self.name)



if __name__ == "__main__":
    p = Person("p")
    s = Student("s")
    print(s.__dict__)
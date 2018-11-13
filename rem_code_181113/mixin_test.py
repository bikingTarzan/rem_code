# -*- coding:utf-8 -*-
__date__ = '2018/11/13 22:11'


class Vehicle(object):
    def run(self):
        print("I can run")


class PlaneMixin(object):
    def fly(self):
        print('I am flying')


class Airplane(Vehicle, PlaneMixin):
    pass


if __name__ == "__main__":
    airplane = Airplane()
    print(Airplane.__mro__)    #(<class '__main__.Airplane'>, <class '__main__.Vehicle'>, <class '__main__.PlaneMixin'>, <class 'object'>)
    airplane.run()      #I can run
    airplane.fly()      #I am flying


# -*- coding:utf-8 -*-
__date__ = '2018/11/3 10:22'


# def run():
#     t1 = yield 1
#     print(11)
#     print(t1)
#     t2 = yield 2
#     print(t2)
#     t3 = yield 3
#     print(t3)
#
# a = run()
# print(next(a))
# a.send("100")




#2 进阶
def t_run():
    for i in range(5):
        yield i

def t_run2():
    for i in range(5, 10):
        yield i

def run():
    t1 = yield from t_run()
    t2 = yield from t_run2()

for v in run():
    print(v)
# a.send("100")

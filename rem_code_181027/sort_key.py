# -*- coding:utf-8 -*-
__date__ = '2018/10/27 14:16'



#第一种
a = [2, 1, 3]
def F(x):         #函数F相当于新建一个列表b为[3,2,4], 这个新B列表排序，直接影响原列表a
    return x + 1

a.sort(key=F)
print(a)        #[1, 2, 3]

#升级
a = [2, 1, 3]
def F(x):
    if x == 1:
        return 100    #给1值排权值最大
    return x + 1

a.sort(key=F)
print(a)        #[2, 3, 1]
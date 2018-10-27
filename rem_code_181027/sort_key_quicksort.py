# -*- coding:utf-8 -*-
__date__ = '2018/10/27 16:15'


def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)

def partition(array, l, r):
    x = array[r]
    i = l - 1                                                   # 1.i从-1开始定位，有当for循环的值小于目标值x的时候， 就把j的值换到i+1的位置
    for j in range(l, r):
        if array[j] <= x:                                       # 2.寻找到小于x的值是，i才加一
            i += 1
            array[i], array[j] = array[j], array[i]             # 3.刚开始原地互换，
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1

temp_list = [1, 2, 3, 2, 6, 4]

quick_sort(temp_list,0, 5)
print(temp_list)
# -*- coding:utf-8 -*-
__date__ = '2018/10/20 11:58'

import os
import multiprocessing
from functools import partial

def target(iterable_item, lock, mem_list):
    for item in range(iterable_item):
        if item == 3:
            lock.acquire()
            n = 10000000
            j = 0
            mem_list.append(11)
            print(id(mem_list), len(mem_list), mem_list, "*")
            # while True:
            #     j+=1
            #     if j == n:
            #         break
            #     mem_list.append("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
            #     print("mem_list:", len(mem_list))
            # print("lock_id:{}".format(id(lock)), os.getpid(), item)

            lock.release()


# def warp_func(func, lock=l, mem_list=mem_list)

def main():
    iterable = [1, 2, 3, 4, 5]
    pool = multiprocessing.Pool(10)
    m = multiprocessing.Manager()
    l = m.Lock()
    mem_list = m.list()
    func = partial(target, lock=l, mem_list=mem_list)
    pool_res = [pool.apply_async(func, (i,)) for i in iterable]
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
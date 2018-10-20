# -*- coding:utf-8 -*-
__date__ = '2018/10/20 11:58'

import os
import multiprocessing
from functools import partial

def target(iterable_item, lock):
    print("pid: {} numbers:{}".format(os.getpid(), iterable_item))
    for item in range(iterable_item):
        print("item:", item)

        if item == 3:
            print(os.getpid(), item)
            lock.acquire()
            print("lock_id:{}".format(id(lock)), os.getpid(), item)
            
            lock.release()

def main():
    iterable = [1, 2, 3, 4, 5]
    pool = multiprocessing.Pool(10)
    m = multiprocessing.Manager()
    l = m.Lock()
    func = partial(target, lock=l)
    pool.apply_async(func, (iterable,))
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
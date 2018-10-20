# -*- coding:utf-8 -*-
__date__ = '2018/10/20 10:44'

import os
import time
import multiprocessing

def target(iterable_item):
    print("pid: {} numbers:{}".format(os.getpid(), iterable_item))
    for item in range(iterable_item):
        print("item:", item)

        if item == 3:
            lock.acquire()
            print("lock_id:{}".format(id(lock)), os.getpid(), item)
            lock.release()

#
def init(l):
    global lock
    lock = l

def main():
    iterable = [1, 2, 3, 4, 5]
    l = multiprocessing.Lock()

    pool = multiprocessing.Pool(processes=10, initializer=init, initargs=(l,))
    multiple_res = [pool.apply_async(target, [i]) for i in iterable ]

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
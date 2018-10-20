# -*- coding:utf-8 -*-
__date__ = '2018/10/20 10:44'

import os
import multiprocessing

def target(iterable_item):
    print("pid: {} numbers:{}".format(os.getpid(), iterable_item))
    for item in range(iterable_item):
        # Do cool stuff
        if item == 3:
            lock.acquire()
            # Write to stdout or logfile, etc.
            lock.release()


def init(l):
    global lock
    lock = l



def main():
    iterable = [1, 2, 3, 4, 5]
    l = multiprocessing.Lock()

    pool = multiprocessing.Pool(initializer=init, initargs=(l,))
    pool.map(target, iterable)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
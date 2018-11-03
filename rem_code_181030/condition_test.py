# -*- coding:utf-8 -*-
__date__ = '2018/10/30 10:21'

import threading


class Ming(threading.Thread):
    def __init__(self, cond):
        super().__init__()
        self.cond = cond


    def run(self):
        with self.cond:
            print("ming 1")
            self.cond.notify()
            self.cond.wait()

            print("ming 2")
            self.cond.notify()
            self.cond.wait()

            print("ming 3")
            self.cond.notify()
            self.cond.wait()


class Red(threading.Thread):
    def __init__(self, cond):
        super().__init__()
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("red 1")
            self.cond.notify()

            self.cond.wait()
            print("red 2")
            self.cond.notify()

            self.cond.wait()
            print("red 3")
            self.cond.notify()

if __name__ == "__main__":
    cond = threading.Condition()

    ming = Ming(cond)
    red = Red(cond)

    red.start()
    ming.start()

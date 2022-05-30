# encoding:utf-8
__author__ = 'Fioman'
__time__ = '2019/3/9 16:52'
from threading import Thread, RLock
import time

rlock = RLock()

class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        rlock.acquire()
        print('{} 拿到了A锁'.format(self.name))
        rlock.acquire()
        print('{} 拿到了B锁'.format(self.name))
        rlock.release()
        rlock.release()

    def f2(self):
        rlock.acquire()
        print('{} 拿到了A锁'.format(self.name))
        time.sleep(2)
        rlock.acquire()
        print('{} 拿到了B锁'.format(self.name))
        rlock.release()
        rlock.release()

if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()
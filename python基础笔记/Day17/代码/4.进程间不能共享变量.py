import multiprocessing as mp
import os
import random
import time

list1 = [10,20,30,40]
# 进程内存空间独立，对于共享的变量，会产生一个副本
def worker():
    global list1
    # current_process() 获取当前进程对象
    print("子进程{}开始".format(mp.current_process().name))
    list1[0] = -10
    print("子进程：",list1)
    print("{}子进程结束".format(mp.current_process().name))
if __name__ == "__main__":
    print("主进程{}开始".format(mp.current_process().name))
    p = mp.Process(target=worker)
    p.start()
    p.join()
    print("list1:",list1)
    print("主进程结束")














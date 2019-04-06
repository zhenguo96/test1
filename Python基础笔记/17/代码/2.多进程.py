import multiprocessing as mp
import os
import random
import time
def worker_1():
    print("子进程1：开始")
    time.sleep(random.randint(1,5))
    print("子进程1：结束")
def worker_2():
    print("子进程2：开始")
    time.sleep(random.randint(1, 5))
    print("子进程2：结束")
def worker_3():
    print("子进程3：开始")
    time.sleep(random.randint(1, 5))
    print("子进程3：结束")
if __name__ == "__main__":
    print("主进程开始")
    p1 = mp.Process(target=worker_1)
    p2 = mp.Process(target=worker_2)
    p3 = mp.Process(target=worker_3)
    # 启动
    p1.start()
    p2.start()
    p3.start()
    print("当前的cpu的核数：",mp.cpu_count())
    # active_children 返回当前活动的进程，是可迭代对象
    for p in mp.active_children():
        print(p.name,p.pid)
    print("主进程结束")












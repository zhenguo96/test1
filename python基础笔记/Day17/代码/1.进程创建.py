import multiprocessing as mp
import os
import random
import time

# 子进程
def run(name):
    # 获取当前进程的进程PID os.getpie()
    print("子进程名：{}，进程pid：{}".format(name,os.getpid()))
    time.sleep(random.randint(1,3))
    print("子进程结束")

if __name__ == "__main__":
    print("主进程（父进程）开始：")
    # 创建进程，被创建的进程叫子进程
    p = mp.Process(target=run,args=("我最帅",))
    # 启动进程
    p.start()
    print("主进程结束")



















import multiprocessing as mp
import os
import random
import time

def worker():
    time.sleep(2)
    print("子进程结束")
if __name__ == "__main__":
    print("主进程开始")
    p = mp.Process(target=worker)
    p.start()
    # 主进程会等p执行完后，在继续执行
    p.join()
    print("主进程结束")




















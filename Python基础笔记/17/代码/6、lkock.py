import multiprocessing
import random
import time

def qiang(filename,lock):
    print("{}开始抢票".format(multiprocessing.current_process().name))
    lock.acquire()
    with open(filename,'r+') as fp:
        piao = int(fp.read().strip())
        piao -= 1
        print("当前剩余{}".format(piao))
        fp.seek(0,0)
        fp.write(str(piao))
        lock.release()
    print("{}结束抢票".format(multiprocessing.current_process().name))

if __name__ == "__main__":
    list1 = []
    lock = multiprocessing.Lock()
    for i in range(5):
        p = multiprocessing.Process(target=qiang,args=('1.txt',lock))
        list1.append(p)
        p.start()

    for j in range(5):
        list1[j].join()























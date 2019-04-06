# 多个进程同时访问共享资源，会造成数据混乱，可以通过加锁解决
import multiprocessing
import random
import time
# 子进程
def qiang(filename):
    with open(filename,'r+') as fp:
        num = int(fp.read().strip())
        num -= 1
        print("当前剩余：{}".format(num))
        time.sleep(random.randint(1,3))
        fp.seek(0,0)
        fp.write(str(num))
    print("进程{}结束抢票".format(multiprocessing.current_process().name))
qiang(r'1.txt')
if __name__ =="__main__":
    print("主进程开始")
    for i in range(10):
        list1 = []
        p = multiprocessing.Process(target=qiang,args=('1.txt'))
        list1.append(p)

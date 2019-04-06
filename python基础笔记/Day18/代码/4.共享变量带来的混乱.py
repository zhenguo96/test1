import random
import threading
import time
# 进程和线程区别：进程之间是相互隔离，不能共享内存
# 同一个主线程中各个子线程共享内存
# list1 = [0,2,3,4]
# # 负责修改列表
# def change():
#     global list1
#     print("\n子线程开始")
#     # list1[0] = 90
#     for i in range(len(list1)):
#         list1[i] = 1
#         time.sleep(random.random())
#     print("\n子线程中：{}".format(list1))
#     time.sleep(1)
#     print("\n子线程结束")
#
# def show():
#     global list1
#     print("{}子线程显示".format(threading.currentThread().name))
#     for i in range(len(list1)):
#         print(list1[i],end=" ")
#         time.sleep(random.random())
#     print("{}显示结束".format(threading.currentThread().name))
#
# if __name__ == "__main__":
#     print("主线程开始")
#     t1 = threading.Thread(target=change,name="change")
#     t2 = threading.Thread(target=show,name="show")
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("\n主线程中：{}".format(list1))
#     print("主线程结束")

list1 = [0]*10
# 负责修改列表
def change():
    global list1
    print("{}子线程开始".format(threading.currentThread().name))
    for i in range(len(list1)):
       list1[i] = 1
       time.sleep(0.2)
       print("{}子线程中：{}".format(threading.currentThread().name, list1))
    print("{}子线程结束".format(threading.currentThread().name))
#显示列表
def show():
    global list1
    print("{}子线程显示".format(threading.currentThread().name))
    # for i in range(len(list1)):
    time.sleep(1)
    print(list1)
    print("{}显示结束".format(threading.currentThread().name))
if __name__ == "__main__":
    print("主线程开始")
    t1 = threading.Thread(target=change,name="change")
    t2 = threading.Thread(target=show,name="show")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("\n主线程：{}".format(list1))
    print("主线程结束")


















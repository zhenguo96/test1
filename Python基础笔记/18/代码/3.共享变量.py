import threading
import time
# 进程和线程区别：进程之间是相互隔离，不能共享内存
# 同一个主线程中各个子线程共享内存
# list1 = 20
# def change():
#     global list1
#     print("子线程开始")
#     # list1[0] = 90
#     list1 = 90
#     print("子线程中：{}".format(list1))
#     time.sleep(1)
#     print("线程结束")
#
# if __name__ == "__main__":
#     print("主线程开始")
#     t1 = threading.Thread(target=change)
#     t1.start()
#     t1.join()
#     print("主线程中：{}".format(list1))
#     print("主线程结束")

list1 = 20
def change():
    global list1
    print("子线程开始")
    # list1[0] = 90
    list1 = 90
    print("子线程中：{}".format(list1))
    time.sleep(1)
    print("子线程结束")

if __name__ == "__main__":
    print("主线程开始")
    t1 = threading.Thread(target=change)
    t1.start()
    t1.join()
    print("主线程：{}".format(list1))
    print("主线程结束")
















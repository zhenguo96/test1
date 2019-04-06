import random
import threading
import time

# threadLocal全局对象
global_data = threading.local()

def sub_thread1():
    global global_dict
    # 定义了一个局部变量
    global_data.num = 9
    time.sleep(2)

def sub_thread2():
    global global_dict
    print(global_data.num)

sub_thread1()
if __name__ == "__main__":
    t1 = threading.Thread(target=sub_thread1,name='t1')
    t2 = threading.Thread(target=sub_thread2,name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()












import random
import threading
import time

global_dict = {}

def sub_thread1():
    global global_dict
    global_dict[threading.currentThread().name] = {}
    global_dict[threading.currentThread().name]['num'] = 9
    print(global_dict)
    time.sleep(2)

def sub_thread2():
    global global_dict
    print(global_dict["MainThread"]['num'])

sub_thread1()
if __name__ == "__main__":
    t1 = threading.Thread(target=sub_thread1,name='t1')
    t2 = threading.Thread(target=sub_thread2,name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()












import threading
class MyThread(threading.Thread):
    def __init__(self,num):
        super().__init__()
        self.num = num

    # 定义run方法，start默认会启动run方法
    def run(self):
        print("hello{}".format(self.num))

if __name__ == "__main__":
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("end")






















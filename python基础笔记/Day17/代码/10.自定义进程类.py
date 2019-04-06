import multiprocessing
import random
import time
# 自定义进程类必须继承
class MyProcess(multiprocessing.Process):
    def __init__(self,name):
        # 调用父类的构造函数
        super().__init__()
        self.name = name

    # 实现run方法，start()会自动调用run方法
    def run(self):
        # 进程的主体
        print("{}开始了".format(self.name))
        time.sleep(random.random())
        print("{}结束了".format(self.name))

if __name__ == "__main__":
    print("主进程")
    p1 = MyProcess("进程1")
    p2 = MyProcess("进程2")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("主进程结束")



















import threading
import time

def work():
    print("启动子线程：{}".format(threading.currentThread().name))
    time.sleep(2)
    print("子线程结束")


if __name__ == "__main__":
    print("主线程")
    # 创建线程
    t1 = threading.Thread(target=work,name="我不是线程")
    # demon 主线程结束，立刻终止子线程
    t1.demon = True
    # 启动线程
    t1.start()
    # 等t1结束，主线程才结束
    t1.join()
    print("主线程结束")














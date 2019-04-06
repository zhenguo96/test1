# python3.4后添加的新模块
from concurrent.futures import ThreadPoolExecutor
import time
def work(num):
    print("haha:%d"%num)
    time.sleep(1)

if __name__ == "__main__":
    # 参数：指定了最大线程数
    excutor = ThreadPoolExecutor(3)
    # for i in range(1,10):
    #     # submit 池子里的线程是并发执行的，顺序不可预测
    #     futurer = excutor.submit(work,i)
    #     futurer.done()
    a = [x for x in range(1,10)]
    with ThreadPoolExecutor(3) as ec:
        # map 是顺序执行的
        ec.map(work,a)

















# import multiprocessing
# import random
# import time
# # 进程池帮助管理多个进程
# # 子进程
# def worker(name):
#     print("{}开始了".format(name))
#     time.sleep(random.random())
#     print("{}结束了".format(name))
#
# if __name__ == "__main__":
#     # 参数是管理的进程数目
#     pool = multiprocessing.Pool(3)
#     print(pool)
#     for i in range(1,6):
#         # 异步（非阻塞）
#         pool.apply_async(worker, args=("进程%d" % i,))
#         # 阻塞方式
#         pool.apply(worker, args=("进程%d" % i,))
#     # 在调用join方法之前，必须调用close，调用close后，池子关闭，不能在往其中添加新进程
#     pool.close()
#     # 等所有进程结束后，主进程才结束
#     pool.join()
#     print("主进程结束")

import multiprocessing
import time
import random
#进程池帮助管理多个进程
#子进程
def worker(name):
    print("进程{}开始了".format(name))
    time.sleep(random.random())
    print("进程{}结束了".format(name))
if __name__ == "__main__":
    p = multiprocessing.Pool(3)
    for i in range(1,6):
        # p.apply_async(worker, args=(i,))
        p.apply(worker, args=(i,))
    p.close()
    p.join()
    print("主进程结束")

# def worker(name):
#     print("{}开始了".format(name))
#     time.sleep(random.random())
#     print("{}结束了".format(name))
#
# if __name__ == "__main__":
#     #参数是管理的进程数目
#     pool = multiprocessing.Pool(3)
#     print(pool)
#     for i in range(1,6):
#         # 非阻塞（异步）
#         # pool.apply_async(worker,args=("进程%d"%i,))
#         # 阻塞方式
#         pool.apply(worker,args=("进程%d"%i,))
#     #在调用join方法之前，必须调用close，调用close后，池子关闭，不能再往其中添加新进程
#     pool.close()
#     #等所有进程结束后，主进程才结束
#     pool.join()
#     print("主进程结束")

















# # 进程队列
# from multiprocessing import Process
# import multiprocessing
# import random
# import time
#
# def eat(q):
#     while 1:
#         res = q.get()
#         if not res:
#             print("{}吃了一个包子".format(multiprocessing.current_process().name ))
#         else:
#             break
#
# def product(q):
#     for i in range(20):
#         print('{}生产了一个包子'.format(multiprocessing.current_process().name))
#         q.put('包子%d'%i)
#         time.sleep(random.random())
# if __name__ == "__main__":
#     q = multiprocessing.Queue(3)
#     e = multiprocessing.Process(target=eat,args=(q,))
#     e.start()
#     # 生产
#     product(q)
#     q.put(None)
    
#进程队列
import multiprocessing
import time
import random
#队列
#入队
q = multiprocessing.Queue(3)  #指定队列的元素目
q.put(10)
q.put(11)
q.put(12)
print(q.full())
# #出队
print(q.get())
print(q.get())
print(q.get())
print(q.empty())

def eat(q):
    while 1:
        #从队列中获取
        res = q.get()
        if  res:
            print("{}吃了{}".format(multiprocessing.current_process().name,res))
        else:
            break
        time.sleep(random.random())
def product(q):
    for i in range(1,10):
        print("{}生产了一个包子{}".format(multiprocessing.current_process().name,i))
        q.put("包子%d"%i)
        time.sleep(random.random())
if __name__ == '__main__':
    # 队列，只能存放3个数据
    q = multiprocessing.Queue(3)
    e = multiprocessing.Process(target=eat,args=(q,))
    e.start()
    # 生产
    product(q)
    # 往队列中方一个None
    q.put(None)
    # e.terminate()  #手动结束
    e.join()
    print("主进程结束")







































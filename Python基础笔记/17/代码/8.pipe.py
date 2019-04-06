# 管道
# import multiprocessing
# import random
# import time
# def eat(p):
#     # 元组解包
#     # 使用right接收
#     left,right = p
#     left.close()    # 关闭left
#     while 1:
#         try:
#             # 从管道中获取
#             res = right.recv()
#             print("{}吃了一个包子".format(multiprocessing.current_process().name ))
#         except EOFError:    # 如果对方不在发送数据
#             right.close()
#             break
#         time.sleep(random.random())
# def product(p):
#     left,right = p
#     right.close()
#     for i in range(20):
#         print('{}生产了一个包子'.format(multiprocessing.current_process().name))
#         # q.put('包子%d'%i)
#         left.send('包子%d'%i)
#         time.sleep(random.random())
# if __name__ == "__main__":
#     p = multiprocessing.Pipe()
#     e = multiprocessing.Process(target=eat,args=(p,))
#     e.start()
#     # 生产
#     product(p)
#     p[0].close()
#     p[1].close()
#     e.join()
#     p.put(None)


#管道
import multiprocessing
import time
import random

def eat(p):
    #元组解包
    # 使用right接收
    left,right = p
    left.close()  #关闭left
    while 1:
        try:
            # 从管道中获取
            res = right.recv()
            print("{}吃了{}".format(multiprocessing.current_process().name, res))
        except EOFError:  #如果对方不在发送数据
            right.close()
            break
        time.sleep(random.random())
def product(p):
    left,right = p
    right.close()
    for i in range(1,10):
        print("{}生产了一个包子{}".format(multiprocessing.current_process().name,i))
        # q.put("包子%d"%i)
        left.send("包子%d"%i)
        time.sleep(random.random())
if __name__ == '__main__':
    # 队列，只能存放3个数据
    p = multiprocessing.Pipe()
    print(p)
    e = multiprocessing.Process(target=eat,args=(p,))
    e.start()
    # 生产
    product(p)
    p[0].close()
    p[1].close()
    e.join()
    print("主进程结束")
































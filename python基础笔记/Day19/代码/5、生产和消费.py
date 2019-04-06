import time
import threading
def product(c):
    """
    
    :param c: 消费者
    :return: 
    """
    print(threading.currentThread().name)
    c.send(None)    # 启动消费者消费
    for i in range(1,11):
        print("生产者生产了数据：%d"% i)
        res = c.send(i)
        print("消费者反馈：已收到数据：{}".format(res))
        time.sleep(1)
    c.close()   # 停止消费者消费

def consume():
    print(threading.currentThread().name)
    res = ""
    while True:
        x = yield res
        if not x:
            return
        print("消费者收到：{}".format(x))
        res = x
c = consume()
product(c)
















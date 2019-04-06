# 3.写一个装饰器，传入一个函数，测量一下这个函数的运行时间
import time
start = time.time()
def magic(func):
    def inner():
        func()
        print("我喜欢吃炸鸡")
        print("我喜欢山珍海味")
    return inner
@magic
def eat():
    print("我喜欢吃水果")
eat()
time.sleep(1)
end = time.time()
print(end-start)








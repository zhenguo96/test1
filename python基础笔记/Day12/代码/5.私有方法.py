class Dog:
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind
    def eat(self):
        # 调用其他方法： self.方法名()
        self.__bite()
    def __bite(self):
        print("别跑，咬不死你")

    # 保护属性，不要通过对象.方法名() 调用
    def _sleep(self):
        print("好吃没过饺子")

    # __方法名__ 系统的方法，不建议自己定义的方法采取这样的名字
dog = Dog("哈士奇",4)
dog.eat()
# 私有方法不能直接通过 对象.方法名() 调用
# dog.__bite()

# 不建议这样调用保护方法
dog._sleep()










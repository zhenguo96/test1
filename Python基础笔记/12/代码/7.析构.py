# 析构方法
# 触发时机：销毁对象的时候自动执行
# 无参，没有返回值
class Animal:
    def __init__(self,name):
        self.name = name
        print(self.name,"构造")
    def __del__(self):
        print(self.name,"析构")

    # 除了self，不需要其他参数
    # 触发时机：对象向字符串转换时自动执行
    def __str__(self):
        return "姓名：{}".format(self.name)
# 最无所畏惧的动物
mihuan1 = Animal('1')
# print(mihuan1)
s1 = str(mihuan1)
print(s1,"ddddd")
# mihuan2 = Animal('2')
# 对象被销毁自动触发析构方法执行
# del mihuan2
# mihuan3 = Animal('3')

# import time
# time.sleep(5)










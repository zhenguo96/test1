class MyInt:
    def __init__(self,num=0):
        self.num = num
    def __rsub__(self, other):
        return MyInt(other - self.num)
    # 重载减法运算符
    def __sub__(self, other):
        return MyInt(self.num - other.num)
    # 重载加法运算符
    def __add__(self, other):
        return MyInt(self.num + other.num)
    # 关系运算符
    # def __lt__(self, other):
    #     return self.num < other.num
    def __str__(self):
        return str(self.num)
a = MyInt(2)
b = MyInt(5)
# print(a + b)        # a.__add__(b)
# print(a < b)
list1 = [MyInt(10),MyInt(15),MyInt(9)]
# list1.sort()
list1.sort(key=lambda x:x.num,reverse=True)
for item in list1:
    print(item)















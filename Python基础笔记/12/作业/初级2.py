# 2.写一个计算器类，可以进行加、减、乘、除计算
class Counter():
    def __init__(self,num1):
        self.num1 = num1
    def add(self):
        return self.num1[0] + self.num1[1]
    def sub(self):
        return self.num1[0] - self.num1[1]
    def mul(self):
        return self.num1[0] * self.num1[1]
    def div(self):
        return self.num1[0] / self.num1[1]
counter = Counter((1,2))
print(counter.add())







from collections import Iterable,Iterator
a = [1,4,32,5]
# 可迭代对象:能用for-in遍历的对象
# for value in a:
#     print(value,end=' ')
# 判定是否是可迭代对象
# print(isinstance("",Iterable))
# print(isinstance([],Iterable))
# print(isinstance({},Iterable))
# print(isinstance(set(),Iterable))
# print(isinstance((),Iterable))

# 迭代器(Iterator)：就是可以使用next函数获取下一个值
# print(next(a))
class A:
    def __init__(self):
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        tmp = self.i
        self.i += 1
        return tmp
a = A()
print(next(a))
# 判定是否是迭代器
print(isinstance(a,Iterator))
print(isinstance([],Iterator))
print(isinstance((),Iterator))

# 可迭代对象转迭代器
gen1 = iter(a)
print(gen1,type(gen1))









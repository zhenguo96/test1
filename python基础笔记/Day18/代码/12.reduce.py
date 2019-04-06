# reduce 对可迭代对象进行统计
import random
from functools import reduce

a = [random.randint(10,20) for i in range(10)]
print(a)
# 用法：
# res = reduce(lambda x,y:x+y,a)
# print(res)

res = reduce(lambda x,y:x+y,a,10)
print(res)


















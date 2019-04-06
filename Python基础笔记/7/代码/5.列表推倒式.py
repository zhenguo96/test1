# 语法
# [express for value in iterable]
# 1-100所有元素组成的list
# l1 = [x for x in range(100)]
# l2 = [x for x in range(100) if x % 2 == 0]
# l3 = [x for x in range(100) if x % 2]

# tmp = []
# for x in range(100):
#     if x % 2 == 0:
#         tmp.append(x)
# print(l2)
# print(l3)
import random
l4 = [random.randint(0,100) for i in range(10)]
print(l4)


# 字典推导式
d1 = {key:value for key,value in zip(['a','b','c'], (9,8,7))}
print(d1)

# 集合推导式
res = {x for x in range(2,10)}
print(res)

#
l = ["Hello", "World", 10, "IBM", "Apple"]
res = [value.lower() if isinstance(value,str) else value for value in l]
print(res)






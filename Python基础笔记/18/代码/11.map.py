# map 内置函数
# 遍历一个可迭代对象，用传入函数处理可迭代对象的每一个元素
# a = [10,23,90,83]
# def mul(x):
#     return 2*x

# 得到一个迭代器
# res = map(mul,a)
# print(res)
# print(list(map(mul,a)))

# map 函数的内部实现
# def tmp(mul,a):
#     for i in range(len(a)):
#         yield mul(a[i])
# res = tmp(mul,a)
# print(res,list(res))

# res = map(lambda x:2*x,a)
# print(list(res))


a = [10,23,90,83]
# res = map(lambda x,y:x+y,a,a[1:])
# print(list(res))

def tmp(func, *args):
    min1 = min([len(x) for x in args])
    for i in range(min1):
        yield func(*[x[i] for x in args])
res = tmp(lambda x,y:x+y,a,a[1:])
print(list(res))












# def fib(n):
#     a = 0
#     b = 1
#     for i in range(1,n+1):
#         a,b = b,a+b
#         # 执行到yield表达式的时候，函数暂停执行，返回后面表达式的值
#         yield a
# # 生成器
# p = fib(10)
# print(p,type(p))
# 获取下一项的数值
# print(next(p))
# 对生成器遍历，只能遍历一遍
# for value in p:
#     print(value)
# for value in p:
#     print(value)

# for value in fib(10):
#     print(value)

# 生成器转列表
# print(list(p))

# 生成器表达式
# （express for x in 可迭代对象）
ge = (x ** 2 for x in range(0,100,2))
print(ge,type(ge))
print(list(ge))
# 不能重复遍历，只能遍历一遍
for value in ge:
    print(value,end=' ')









# 元组元素赋值给变量，这就是所谓的解包
# t1 = (10,20,30)
# t1 = 10,20,30       # 定义了一个(10,20,30)
# a,b,c = t1
# a, b = 2, 3
# a, b = b, a
# print(a,b,c)

# 元组元素多于变量个数
# a, b, *last = 10, 20, 30, 40
# # _变量接受其余所有元素，组成一个列表
# print(a,b,last)
# print(type(last))
# a, *_, b = 10, 20, 30, 40
# print(a,_,b)

# 列表解包
# a,b = [10,20]
# print(a,b)
# a,b,*_ = [1,2,3,4,5]
# print(a,b,_)
#
# # 字符串解包
# a, b, *_ = "hello"
# print(a,b,_)
#
# # range
# a,b, *_ = range(5)
# print(a,b,_)

grade = [
    ('小风', 90),
    ('黄毅', 87),
    ('金庸', 67)
]

for name,score in grade:
    print(name,score)





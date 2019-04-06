# 身份运算符
a = 10
b = 10
# 如果a和b指向相同的对象，返回True，否则返回False
print(id(a), id(b))
print(a is b)

# is not
# 如果a和b指向不同的对象，返回True，否则返回False
print(a is not b)

# is 和判等的区别
a = 10
b = 10.0
print(id(a), id(b))
# 判断两个变量的地址是否相等
print(a is b)

# 判断两个变量的值是否相等
print(a == b)

# 成员运算符
a = [1,2,3,4,5]
# 判断一个变量是否是集合的成员，如果是返回True，否则返回False
print(3 in a)
print(10 not in a)

# if else表达式
a = 16
b = 5 if a < 15 else 20
print(b)
# if a < 15:
#     b = 5
# else:
#     b = 20


# 深复制和浅复制
import copy
# 不可变对象：int float boolean str tuple
# 不可变对象不存在深浅复制
# a = 10
# b = a
# # copy是浅拷贝
# c = copy.copy(a)
# print(id(a),id(b),id(c))

# s1 = "ok"
# s2 = copy.copy(s1)
# print(id(s1),id(s2))

# 可变对象，list,dict,set 容器
a = [1,[5,6],3]
# 浅拷贝 只拷贝容器，不拷贝元素
b = copy.copy(a)
# print(id(a),id(b))
a[0] = 10
a[1][0] = 10
print(a,b)
# print(id(a[1]),id(b[1]))

# 深拷贝，即复制容器也复制元素（元素必须是可变对象）
c = copy.deepcopy(a)
print(id(a),id(c))














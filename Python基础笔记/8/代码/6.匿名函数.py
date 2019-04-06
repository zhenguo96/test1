# 匿名函数：没有函数名的函数
# lambda 参数列表：一个表达式
# 使用场景：函数体非常简单，只用一个表达式就能完成，可以使用lambda简化函数定义
func = lambda a,b:a+b
# 等价函数定义
# def add(a,b):
#     return a + b
# print(add(3,5))
# print(func(3,5))
action = [0,(lambda a,b:a+b), (lambda a,b:a-b), (lambda a,b:a*b), (lambda a,b:a/b if b<0 or b>0 else "除数不能为0")]
print(action[1](3,4))

# 乘法
a = (lambda a,b:a+b)(2,4)
print(a)







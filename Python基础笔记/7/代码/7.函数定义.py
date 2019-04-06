# 函数定义
# def 函数名(变量名1,变量名2...):
#     函数体(实现函数功能的代码段)
"""
1.函数体必须缩进
2.函数名的命名规则：同变变量命名的规则
3.不要使用系统函数名
4.如果函数由多个单词组成一般用下划线分割：get_area
"""
def area(r):
    import math
    result = math.pi * r * r
    return result
res = area(10)
print(res)

# 不要和系统函数重名，否则系统函数无法使用
# def print():
#     pass
# print(10,30)

# 定义一个函数，完成两个数相加，返回和
def sum1(num1,num2):
    sum2 = num1 + num2
    return sum2
res = sum1(1,2)
print(res)

"""
函数功能：
参数：传两个参数
返回值 两个数的和
"""






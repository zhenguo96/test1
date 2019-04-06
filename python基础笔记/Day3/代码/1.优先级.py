# a = 1 and 5
# print(a)
# 类型转换
# 一个运算符两边的数据类型必须一致，否则报错
# print(22 + 'ok')
# print(22 > 'ok')
# 系统自动进行的转换，一般称之为自动类型转换
# bool --> int --> float
# print(1 + 2.3 + True)
# print(1 + 2.3 +False)
# print(1 + True)

# 逻辑运算符
# print(0 and 'app')

# 手动类型转换
# 把其他类型转换为整型
print(int(2.3) + 2)    # float --> int 直接抹去小数点
# 怎么实现四舍五入
# a = 2.55
# print(int(a + 0.5))
# 字符串转整数    字符串中只能包含+/-或纯数字，不能包含其他字符
a = int('-12')
print(a, type(a))

# bool
# True ==> 1    False ==> 0
print(int(True))
print(int(False))

# 其他类型转浮点数
# int ==> float
print(float(12))

# bool ==> float
print(float(True))

# str ==> float     字符串不能包含除+/-小数点之外的其他字符
print(float('-12.3'))
# print(float('-12.3$'))

# 其他类型转bool
# 非0、0.0、空字符转为True, 0转为False
print(bool(3), bool(0.0))
print(bool('ok'), bool(''))

# 其他类型转字符串
print(str(True), type(str))
print(str(1), str(1.4))

# eval 可以把字符串当代码执行，但字符串中不能定义变量
b = 23
eval('print(b)')






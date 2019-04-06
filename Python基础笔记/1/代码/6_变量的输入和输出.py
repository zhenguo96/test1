# 变量的输入
# input只能输入字符串
# 参数用于提示用户输入的内容，可以没有提示
# name = input("请输入用户名：")
# print(name)
# age = input("请输入你的年龄：")
# print(age+"11")

# 变量的输出 print
# print 会自动换行
# 1 输出字符串到屏幕
print("hello")
# 2 输出变量到屏幕
a = 3
b = 5
print(a, b)
# 3 输出变量和值
print("a = ", a, b, "end")

# 格式化输出
age = 21
name = "name1"
money = 198453234.21
# %s 字符串占位符
# %d 整数占位符
# %f 实数占位符
print("我叫%s,我今年%d岁,我有%.2f的存款" % (name,age,money))
# 如果只有一个变量，小括号可以不加
print("我叫%s" % name)






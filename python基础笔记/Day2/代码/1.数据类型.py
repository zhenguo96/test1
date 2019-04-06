# 不同类型的数据不能直接运算
# a = 10
# name = "tom"
# res = a + name

# 1.数值型
# 1.1 整型
a = 10
b = -4
# 1.2 浮点数
c = 1.2
# 科学计数法
# e后必须是整数
b = 1e6 # 1*10^6, e表示以10为底的整数
b = 1.2e2
# print(b)

# 1.3 复数
a = 1 + 2j

# 字符串
name = 'tom'
name = "lilei"

# 转义字符
# 字符串界定符：单引号、双引号、三引号
# 不能正常表示的字符，\t   \b   \n    \r    \a    \\
name = 'to\'m'
poem = "he\"ll\"o"
# \b 退格键
print("hello\tworld\b")
# \r 回车，光标返回行首
print("hello world\r123")
# \n 换行
print("hello\nworld")
# 运算
a = "123"
b = "234"
# 字符串拼接，产生一个新字符串
res = a + b
print(res)

# 布尔类型 表示真假
isMan = True
isFlag = False

isCloud = False
if isCloud:
    # 如果条件为真，执行这
    # 代码必须缩进
    print("sleep")
else:
    # 条件为假执行这
    print("go")

# None 表示变量未赋值，不是0，也不是空字符
a = None
if a == None:
    print("no")
    a = 10
else:
    print(a)




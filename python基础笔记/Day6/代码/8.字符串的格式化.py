# 字符串格式化
# %
name = "tome"
age = 21
# intro = "我叫%5s，我今年%-6d岁" % (name,age)
# print(intro)
# 四舍五入
# res = 123.1451637
# res = "%15.4f"%res
# print(res)

# width = int(input("请输入列宽："))
# a = 20
# print("%*d"%(width,a))


# format
age = 123456789
# res = "我叫{:o>10}，我今年{:0^20,}岁".format(name, age)
res = "我叫{name}，我今年{age}岁".format(name='123', age=12)
print(res)


# 判断变量类型
# 1 type
# 功能：返回变量或值的类型
print(type(10))
# 用于类型判断
a = 10
if type(a) is int: # 如果a是整型，
    a += 2
    print(a)
else:
    print("error")

# isinstance(obj, typename)
a = 10
if isinstance(a,float):
    print("是float")
else:
    print("不是float")















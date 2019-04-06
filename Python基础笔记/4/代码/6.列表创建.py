# 列表（list）：有序数据的集合
# 1 创建
grade1 = [60, 70, 90, 93.4]
grade2 = []     # 空列表
grade3 = list() # 空列表
grade4 = list("hello")  # 可以把字符串、元组、字典等转换为列表
print(grade1)

# 2 成员访问
# 列表不能整体访问，只能访问成员
"""
 -4  -3  -2  -1     从右向左下标编号
[60, 70, 90, 95.2]
 0   1   2   3      从左向右下标编号
"""
# 通过下标访问元素
print(grade1[1], grade1[3])
# 下标不能越界
# 4超过了最大下标
# print(grade1[4])

# 访问： 读取或者是修改
grade1[1] = 75
print(grade1)

# 3 遍历： 访问列表所有的元素
# i = 0
# while i < 4:
#     print(grade1[i])
#     i += 1

# for - in
# 只能访问列表的元素值，得不到元素下标
# for value in grade1:
#     print(value)
#     value += 10     # 不能通过修改value修改列表元素的值
# print(grade1)

# 同时访问元素的值和下标
for index, value in enumerate(grade1):
    print(index, value)
    grade1[index] += 10
print(grade1)




# a = [
#     [23,30],
#     [30,10],
#     [14,321],
#     [26,70],
# ]
# def tmp(list1):
#     return list1[1]
# a.sort(key=tmp)
# # key 指是排序的依据，需要出入一个函数，用函数的返回值排序
# # a.sort(key=lambda b:b[1])
# print(a)

# 列表套字典
# grades = [
#     {'name':'李四','age':20,'math':95},
#     {'name':'张三','age':22,'math':99},
#     {'name':'老王','age':52,'math':91},
# ]
# def grade(elem):
#     return elem['age']
# grades.sort(key=grade)
# print(grades)

# 按字符串长度排序
# s1 = ['helsdl','llsjf','alsf','iashoisa']
# s1.sort(key=len)
# print(s1)

# 基础版
# 冒泡排序
# 相邻元素比较，逆序（前大后小）则交换
# 一趟排序，从左往右，相邻的两个元素逆序则交换，

# def mysort(a):
#     for i in range(len(a)-1):
#         for j in range(len(a)-1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j+1] = a[j+1], a[j]
# mysort(a)
# print(a)

# def mysort(a):
#     for i in range(len(a)-1):
#           不再和后面有序元素比较
#         for j in range(len(a)-1-i):
#             if a[j] > a[j + 1]:
#                 a[j], a[j+1] = a[j+1], a[j]
# mysort(a)
# print(a)
# a = [41,12,63,75,23,43,12,543,123,2,45]
# def mysort(a,reverse):
#     for i in range(len(a)-1):
#         isseq = True
#         for j in range(len(a)-1-i):
#             if reverse == True:
#                 if a[j] > a[j + 1]:
#                     a[j], a[j+1] = a[j+1], a[j]
#                     isseq = False
#             else:
#                 if a[j] < a[j + 1]:
#                     a[j], a[j+1] = a[j+1], a[j]
#                     isseq = False
#         if isseq:
#             break
# mysort(a,reverse=False)
# print(a)

d = {1:2,2:1}
print(d.keys())





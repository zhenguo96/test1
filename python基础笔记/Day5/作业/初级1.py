# 1.自定义一个数字列表，获取这个列表中的最小值
list1 = [222, 3, 43, 13, 54, 23, 65, 11]
min1 = list1[0]
for i in range(len(list1)):
    if min1 > list1[i]:
        min1 = list1[i]
print(min1)









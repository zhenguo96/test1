# 2.自定义一个10个元素的数字列表，找出列表中最大数连同下标一起输出
list1 = [1, 2, 3, 4, 5, 66, 7, 8, 9, 10]
max1 = 0
index1 = 0
for i in range(len(list1)):
    if list1[i] > max1:
        max1 = list1[i]
        index1 = i
print(index1)
print(max1)






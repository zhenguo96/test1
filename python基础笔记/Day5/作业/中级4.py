# 4.自定义一个列表，最大的与第一个元素交换，最小的与最后一个元素交换，输出列表
list1 = [54, 3, 43, 13, 222, 23, 65, 11]
max1 = max(list1)
min1 = min(list1)
ma = list1.index(max1)
mi = list1.index(min1)
list1[ma], list1[0] = list1[0], list1[ma]
list1[mi], list1[len(list1)-1] = list1[len(list1)-1], list1[mi]
print(list1)













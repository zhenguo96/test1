# 3.自定义一个数字列表，求列表中第二大数的下标
list1 = [222, 3, 43, 13, 54, 23, 65, 11]
list2 = list1[:]
list2.sort(reverse=True)
while len(list1) - 1:
    i = 1
    if list2[0] != list2[i]:
        max2 = list2[i]
        break
    i += 1
index1 = 0
for j in range(len(list1)):
    if max2 == list1[j]:
        print(index1)
    index1 += 1




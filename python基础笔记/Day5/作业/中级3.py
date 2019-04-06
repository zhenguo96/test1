# 1. 循环移位
#   有n个元素的列表，使其前面m个元素顺序移动到列表尾部，后面n-m个数移动到最前面，要对m的值进行校验。
# [1, 2, 3,4,5,6]
# m=3
# [4,5,6,1,2,3]
n = [1, 2, 3, 4, 5, 6, 7]
m = 3
list1 = []
for i in range(m):
    list1.append(n[i])
del n[0:m]
n.extend(list1)
print(n)









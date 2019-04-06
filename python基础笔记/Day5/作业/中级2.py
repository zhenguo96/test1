# 给定一个列表：将列表中指定的某个元素全部删除
list1 = [222, 3, 43, 3, 13, 13, 54, 23, 65, 13]
print(list1)
delate = int(input("请输入要删除的元素："))
for i in range(9):
    if delate in list1:
        list1.remove(delate)
print(list1)




# 8.输入两个字符串，从第一字符串中删除第二个字符串中所有的字符
list1 = list("hello sunck")
list2 = list("sunck is a good man")
for i in range(len(list2)):
    if list2[i] in list1:
        j = list1.index(list2[i])
        list1.remove(list1[j])
print(''.join(list1))












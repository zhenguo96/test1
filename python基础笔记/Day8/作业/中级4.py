# 4.自定义一个函数将传入的两个有序列表[1,5,7,9]和[2,2,6,8]合并一个有序列表，比如：[1,2,2,3,6,7,8,9]
list1 = [1,5,7,9]
list2 = [2,2,6,8]
def hb(ls1,ls2):
    ls = ls1 + ls2
    ls.sort()
    return ls
res = hb(list1,list2)
print(res)










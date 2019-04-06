'''
4.数字循环左移，人一个给一个5位整数，比如12345，将该数左移3得到45123，左移两位得到34512，要求实现给定随机左移位数，输出左移后的数字
12345
23451
34512
45123
'''
num = int(input("请输入一个5位整数："))
n = int(input("请输入左移位数："))
list2 = []
list1 = list(str(num))
for i in range(5):
    new = list1[i - n + 1]
    list2.append(new)
    i += 1
newnum = ''.join(list2)
print(newnum)












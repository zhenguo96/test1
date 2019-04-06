# 2.斐波那契数列指的是这样一个数列：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …；这个数列从第三项开始，每一项都等于前两项之和。写一个函数，传入项数n，返回第n项的值
n = int(input("n="))
def fb(n):
    list1 = [1,1]
    for i in range(2, n):
        list1.append(list1[i-1]+list1[i-2])
    return list1[-1]
res = fb(n)
print(res)











# filter 根据函数的返回去除可迭代对象中不满足条件的元素
a = [29,37,23,89,74,23]
res = filter(lambda x:x%2==0,a)
print(res)
print(list(res))

# 找出1-1000内所有的回文数
print(list(filter(lambda x:str(x)==str(x)[::-1],range(1,1001))))















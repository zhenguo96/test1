# 传入函数
def add(a,b):
    return a + b
def opperate(a,b,func):
    """
    
    :param a: 第一个数
    :param b: 第二个数
    :param func: 运算，需要传入一个函数：传入函数
    :return: 
    """
    return func(a,b)
res = opperate(2,5,add)
print(res)





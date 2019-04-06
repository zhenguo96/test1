# 函数不返回值，系统默认返回None
# def add(a,b):
#     print(a + b)
# res = add(2,3)
# print(res)

# def add(a,b):
#     # 返回值，只能有一个返回值
#     # 结束函数调用
#     return a + b
#     print("hello")
# res = add(3,2)
# print(res)

# def add(a,b):
#     if a < 0:
#         return -a + b
#     else:
#         print("hello")
#         return 10

def demo9(a,b):
    """
    文档字符串的例子
    :param a: 
    :param b: 
    :return: 
    """
    # 只是返回一个元组
    return 1,2,3,4
res = demo9(3,4)
print(res)
print(demo9.__doc__)



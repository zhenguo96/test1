# def outter():      # 外部函数
#     a = 1
#     def inner():    # 内部函数
#         print(a)
#     inner()
# # inner() # error
# outter()

def outter():
    a = 1
    def inner():
        print("inner",a)
    return inner
# 得到内部函数的地址

res = outter()
print(res.__closure__)
# 外部函数返回内部函数
# 指内部函数和外部变量构成的整体，是一个对象，在程序运行期间始终存在
res()   # 调用内部函数









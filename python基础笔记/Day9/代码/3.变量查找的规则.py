a = 3
c = 6
def outter():
    a = 1
    b = 3
    print("outter",a,b)
    def inner():
        b = 5
        print("inner",b)
        print("c=",c)
        print("a=",a)
    inner()
# 变量查找规则：从变量引用的地方开始往上找，找力它最近的变量
outter()
print(a,c)











import sys
print(len(sys.argv) - 1)
print(sys.argv)

def demo6(a,b,**kwargs):
    pass
demo6(1,2)
# 关键字参数是指实参
# 关键字参数后不能再跟位置参数
demo6(b=2,a=2)
# 关键字参数后不能再跟位置参数
# demo6(b=2,a=2,5)






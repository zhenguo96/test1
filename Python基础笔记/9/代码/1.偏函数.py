import functools
# 偏函数
def demo(a,b,c,d):
    print(a,b,c,d)

# def partial_demo(a,b):
#     demo(a,b,3,4)
#
# partial_demo(1,2)

#　实现偏函数
# 固定a 和 b
# demo = functools.partial(demo,5,6)
# demo(10,30)

# 固定c和d
demo = functools.partial(demo,c=3,d=5)
demo(1,2)

# 固定任意参数
demo = functools.partial(demo,b=5,c=6)
# 必须使用关键字参数
demo(a=3,d=5)


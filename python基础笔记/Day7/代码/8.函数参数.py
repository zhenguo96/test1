def add(x,y):
    return x + y
res = add(3,4)

"""
形参：函数定义的时候小括号里的变量
实参：函数调用的时候小括号里的变量或数值
"""
#1 实参和形参一一对应,实参向形参传值是从左向右传递
#2 形参不是必须的

# 实参
def demo(name,age,sex):
    print("我叫{},今年{},性别：{}".format(name,age,sex))
# 1.位置参数：实参和形参从左向右一一对应，循序应该一致
demo("tom",21,"男")
#2.关键字参数：为了避免位置参数带来的限制，
a1 = 31
b1 = "tom"
c1 = '女'
demo(name=b1, age=a1, sex=c1)
# 关键字参数写法：形参名=值（常量或变量），顺序随意，形参和实参数量一致

# 默认值
def demo(name,height,sex="男"):
    print(name,height,sex)
# 如果形参有默认值，实参可以不传值，形参就使用默认值
demo('小月月',1.7)     # 小月月 1.7 男
# 如果sex有实参，使用实参的值
demo("郭德纲",1.6,"女")
# 有默认值的形参必须在最右边
# def demo1(name,sex="男",height):
#     pass
# demo("郭德纲",1.6)

# 默认值不可以是可变对象
# 默认值只在第一次调用的时候计算
def demo2(a, b = []):
    b.clear()
    b.append(a)
    print(a,b)
# demo2(1)
# demo2(2)
# demo2(3)

# 可变参数
# *args 表示可以传递任意位置参数
def demo3(a,*args):
    print(a,args)
    # for value in args:
    #     print(value)
demo3(1,2,3,4)
demo3(*[1,2,3,4])

# 任意关键字参数
# kwargs 表示实参可以传递任意关键字参数
# kwargs 是字典
def demo4(a,**kwargs):
    print(a,kwargs)
demo4(5,b=2,c=4,d='l')

#　位置参数、默认值参数、*args,**kwargs
# def demo5(a=5,b,*args,**kwargs):      # error
#     print(a,b=5,*args,**kwargs)
# def demo5(a,b=5,**kwargs,*args):        # error
# 不推荐
# def demo5(a,*args,b=5,**kwargs):
#     print(a,args,b,kwargs)
# demo5(1,(2,3),4,4,5)
# 推荐
def demo5(a,b=5,*args,**kwargs):
    print(a,b,args,kwargs)
demo5(1,2,3,4,5,5,6,)
# 位置必须在关键字参数之前



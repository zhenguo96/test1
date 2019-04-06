# 函数的类型：function
# 函数名就是函数类型的一个实例，是一个变量
def demo():
    print("demo")
print(type(demo),demo)

# 可以修改函数名，但不能再调用了
# demo = 5
# demo()
# 把函数名赋值给其他变量，加括号就可以调用
# pf = demo
# pf()

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def divid(a,b):
    if b<0 or b>0:
        return a / b
    return "除数不能为0"

    action = [0,add,sub,mul,divid]
    if 0<=choice<=4:
        apf = action[choice]
        print(apf(a,b))

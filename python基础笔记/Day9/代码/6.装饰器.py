# 要增强功能的函数
# def eat():
#     print("我喜欢吃水果")

# 装饰器
# func 是需要验证函数
# 必须把要增强的函数传进来
def magic(func):
    def inner():
        func()      # 原来的函数
        # 增强的功能
        print("我喜欢吃j")
        print("我喜欢吃啥")
    return inner
# eat = magic(eat)
# eat()
@magic  # @外部函数 eat = magic(eat)
def eat():
    print("我喜欢吃aaa")
eat()







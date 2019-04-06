def magic(func):
        # 如果带参数，inner与其一致
    def inner(i):
        func(i)
        print("我喜欢吃j")
        print("我喜欢吃啥")
    return inner
@magic
def eat(food):
    print("我喜欢吃{}".format(food))
eat("123")













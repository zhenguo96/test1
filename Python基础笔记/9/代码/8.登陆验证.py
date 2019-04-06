# 装饰器
# func 是需要验证函数
def check_login(func):
    def inner(password):
        # 验证
        if password == "123":
            func(password)
        else:
            print("不能通过，重新验证")
    return inner

@check_login
def forum(password):
    print("发帖：")

@check_login
def comment(password):
    print("jjjjjjjjjj")
forum('123')



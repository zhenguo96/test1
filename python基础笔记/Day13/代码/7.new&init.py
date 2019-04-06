class Cat:
    # 是类方法，用于创建对象
    def __new__(cls, *args, **kwargs):
        print("new:创建对象")
        # 一定要调用父类的new进行对象的创建
        # return super().__new__(cls, *args, **kwargs)
        return super().__new__(cls, *args, **kwargs)
    def __init__(self):
        print("init:初始化对象")
cat = Cat()


















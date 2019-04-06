def demo():
    pass
class Pig:
    def __call__(self, *args, **kwargs):
        print("gggggggggg")
        print(args,kwargs)
p1 = Pig()
p1()
p1(10,a=6)
# callable 测试一个对象是否可调用
print(callable(p1))
print(callable(demo))
















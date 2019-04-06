# 自定义异常类
class CustomException(Exception):
    # 1.自定义构造方法
    def __init__(self,msg=''):
        # 调用父类的初始化方法
        super().__init__()
        self.msg = msg
    # 2 重写str
    def __str__(self):
        return self.msg
    # 3 自定义异常处理方法
    def handle1(self):
        print("异常处理方法")
try:
    raise CustomException("性情不好")
except CustomException as e:
    e.handle1()












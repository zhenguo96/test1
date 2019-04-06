class Person:
    # 构造方法
    """
方法和函数的区别：  方法第一个参数必须是self，函数没有self
                    方法定义在类中，作用域属于类，可以和函数重名
                    方法必须通过对象调用  对象.方法()
    """
    def __init__(self,name,age,sex):
        # 成员属性定义在构造函数中
        # self.属性名 = 属性值
        self.name = name
        self.age = age
        self.sex = sex
    # 行为：
    def eat(self):
        print("吃饭")
    def sleepiing(self):
        print("睡觉")
    def da_doudou(self):
        print("打豆豆")
# 实参和__init__形参一一对应，不算self
xiaoming = Person('小明','12','男')
print(xiaoming.name,xiaoming.age)










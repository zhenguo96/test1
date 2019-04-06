"""
类：人
    属性（静态特征）：
        姓名
        性别
        年龄
    行为（动态特征）：
        吃饭
        睡觉
        打豆豆
"""
"""
1.类名命名规范：
    数字、字符、下划线组成、不能以数字开头
    不能是保留字
    区分大小写
2.命名风格：大驼峰：每个单词首字母大写
3.类体：以冒号开头，必须缩进
"""
class Person:
    # 构造方法
    """
方法和函数的区别：  方法第一个参数必须是self，函数没有self
                    方法定义在类中，作用域属于类，可以和函数重名
                    方法必须通过对象调用  对象.方法()
    """
    def __init__(self):
        # 成员属性定义在构造函数中
        # self.属性名 = 属性值
        self.name = '我'
        self.age = 5
        self.sex = '男'
    # 行为：
    def eat(self):
        print("吃饭")
    def sleepiing(self):
        print("睡觉")
    def da_doudou(self):
        print("打豆豆")

# 实例化对象:类名()
doudou = Person()
print(doudou,type(doudou))

# 调用属性：对象.属性
print(doudou.name,doudou.age)

# 调用方法：对象.方法()
doudou.eat()
doudou.sleepiing()
doudou.da_doudou()









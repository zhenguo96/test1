class Girl:
    def __init__(self,name,age):
        # 公有属性
        self.name = name
        # 私有属性，不能通过对象.__age调用
        self.__age = age
    # getter方法
    def get_age(self):
        return self.__age   # 类内方法里不区分公有和私有

    # setter
    def set_age(self,age):
        self.__age = age

xiaohong = Girl('小红',18)
# 公有属性可以直接通过 对象.属性名 访问
# print(xiaohong.name)
# xiaohong.name = '小芳'
# print(xiaohong.name)

# 私有属性无法通过 对象.属性名
# print(xiaohong.__age)
# 可以通过 对象._类名__属性名 访问
# print(xiaohong._Girl__age)      # 不建议用
print(xiaohong.get_age())
xiaohong.set_age(20)
# print(xiaohong)

# 查看对象的属性
print(xiaohong.__dict__)








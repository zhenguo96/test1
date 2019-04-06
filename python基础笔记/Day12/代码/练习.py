"""
女朋友类：
    属性：
        姓名：
        年龄：
        身高：
    行为：
        做饭
        花钱
"""
# class GirlFriend():
#     def __init__(self,name,age,height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def eat(self):
#         print("我在吃")
#     def money(self):
#         print("我在买")
# girl = GirlFriend("女友1号",18,170)
# print(girl.name,"   年龄:",girl.age,"   身高:",girl.height)
# girl.eat()

# class Person:
#     def __init__(self, name):
#         self.name = name
#     # self 代表当前对象，谁调用这个方法谁就是当前对象
#     def drive(self,car):
#         car.run()
#         print("{}开车去东北".format(self.name))
#     def sing(self):
#         print("丝氨酸框架")
#         return self
# class Car:
#     def __init__(self,brand):
#         self.brand = brand
#     def run(self):
#         pass
# shixiong = Person("孙师兄")
# # print(shixiong.name)
# car = Car("宝马")
# # shixiong.drive(car)
# # 方法的串联调用，连贯调用，前提是sing方法必须返回self
# shixiong.sing().drive(car)

# class Person():
#     def __init__(self,name):
#         self.name = name
#     def fps(self,moster):
#         print("一边射击")
#         moster.unfps()
#     def spear(self):
#         print("{}一边唱歌".format(self.name))
#         return self
# class Moster():
#     def __init__(self,name):
#         self.name = name
#     def unfps(self):
#         print("{}血量-1".format(self.name))
# person = Person("我")
# moster = Moster("怪物")
# person.spear().fps(moster)

# 练习
# 自定义一个圆类
# 1.计算圆的面积和周长
# 2.判断两个圆是否相切、相交、相离
class Circle:
    def __init__(self,r,xy):
        self.r = r
        self.xy = xy
    def s(self):
        s = 3.14 * self.r ** 2
        return s
    def l(self):
        l = 3.14 * 2 * self.r
        return l
    def judge(self,c2):
        distance = ((self.xy[0] - c2.xy[0]) ** 2 + (self.xy[1] - c2.xy[1]) ** 2) ** 0.5
        if abs(distance - c1.r - c2.r) < 1e-7:
            return 1    # 相切
        elif distance > c1.r + c2.r:
            return 2    # 相离
        elif distance < c1.r + c2.r:
            return 3    # 相交
c1 = Circle(5,(1,3))
c2 = Circle(5,(100,100))
res = c1.judge(c2)
print(res)
# print(c1.l())
# print(c2.s())
















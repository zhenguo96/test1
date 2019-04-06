# 3.设计两个类：
# - 一个点类，属性包括xy坐标。
# - 一个Rectangle类（矩形）,属性有左上角和右下角的坐标，可以计算矩形的面积；可以判断点是否在正方形内
#   实例化一个点，一个正方形，输出正方形的面积，输出点是否在正方形内
# class Dot():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# class Rectangle():
#     def __init__(self,xy2):
#         self.xy2 = xy2
#     def s(self):
#         return self.xy2[0] * self.xy2[1]
#     def judge(self,rec2,dot):
#         if (abs(dot.x) < abs(self.xy2[0]) and abs(dot.x) < abs(rec2.xy2[0])) or (abs(dot.y) < abs(self.xy2[1]) and abs(dot.y) < abs(rec2.xy2[1])):
#             return '在正方形内'
#         else:
#             return '不在正方形内'
# dot = Dot(1,2)
# rec1 = Rectangle((2,4))
# rec2 = Rectangle((-2,-4))
# res = rec1.judge(rec2,dot)
# print(res)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectanle:
    def __init__(self,left,right):
        """
        
        :param left: 
        :param right: 
        """
        self.left = left
        self.reight = right

    def area(self,dot):
        return dot.x > self.left[0]and dot.x < self.reight[0] and(dot.y) > self.right[1] and dot.y < self.left[1]

deo = Point(12,3)
dot = Point(2,3)
rec = Rectanle((0,10),(10,0))
print(rec.judge(0,10))
























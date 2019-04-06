# 4.定义一个Time类，成员属性包括：时、分、秒；成员方法：
#     add_hour(self,num)   把小时加num
#     add_minute(self,num) 把分钟加num
#     add_second(self,num) 把秒数加num
#     重写__str(self)__方法，返回格式化的时间字符串："04:16:09"
class Time():
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def add_hour(self,num):
        self.hour += num
        if self.hour >= 24:
            self.hour %= 24
        return self.hour
    def add_minute(self,num):
        self.minute += num
        if self.minute >= 60:
            self.minute %= 60
            self.hour += self.minute // 60
        return self.minute
    def add_second(self,num):
        self.second += num
        if self.second >= 60:
            self.second
        return self.second
    def __str__(self):
        return self.add_hour,self.minute,self.second
t = Time(23,59,59)











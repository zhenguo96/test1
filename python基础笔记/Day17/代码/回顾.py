# 正则：
# 1 原子
# \d 0-9 \w 数字、字母、下划线   \s 空开字符[ \n\r\t]
#[a-c8-9]
import re
# print(re.match(r'[1-9]\d{4,11}$',"23414"))
# 元字符
#{m}    {m,n}   {m,}
# * {0,}    + {1,}      ? {0,1}
# 子元素
# print(re.match(r'(\w+)\w\1',"123b123"))

# 模式修正符
# 如果同时使用多个模式修正符，可以这样写：re:S|re.I
print(re.search(r'he.lo',"dkslhE\nloa",re.S|re.I))
# url匹配

# 无命名组  一个元素就认为是一个组
# 表达式中一个括号就是一个子元素
# s1 = "(\w+)--(\w+)(w+)"
# res = re.match(s1,"kkdkd--23424--;lsadj;lkfaj")
# print(res.group(1),res.group(2),res.group(3))
# print(res.group())
pattern = r'http://www.baidu.com/(\w+)'
route = "http://www.baidu.com/file1"
res = re.match(pattern,route)
print(res.groups())

# 命名组
patter = r'http://www.baidu.com/<?Pfileme>'









# group | groups
import re
s1 = "0310-7484384"
# 在正则规则中，一个小括号就是一个子元素，从左向右编号是1，2，3.......
# r'(\d{3,4})-(\d{7,8})'    # 无命名组
# res = re.match(r'(\d{3,4})-(\d{7,8})',s1)
# print(res)
# print(res.groups())
# # 根据编号提取指定子元素
# print(res.group(1),res.group(2))

# www.baidu.com/2/3
#(\w+\.)+.(com|net|cn)/(\d+)/(|d+)


# 命名组
# www.blog.com/P<name>(tom)/P<age>(21)
#
# s1 = "www.baidu.com/tom/21"
# res = re.match(r'(\w+\.)+com/(?P<name>\w+)/(?P<age>\d+)',s1)
# print(res)
# # 匹配后的键值字典
# print(res.groupdict())
# print(res.group('name'))
# print(res.group(2))


#compile
# 1.验证正则表达式
res = re.compile(r"0211-\d{8}")
for i in range(10000):
    # 2 匹配字符串
    print(res.match("0211-9847564312"))







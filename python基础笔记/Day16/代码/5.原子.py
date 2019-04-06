# 原子：正则表达式最小的组成单位,任何一个字符都是原子，但有些特殊字符需要转义
# * ? |^ $
import re
# s1 = "kahsf;hal;sfh;oashfo;helloklsdakfasfd"
# pattern = "\*"
# if re.search(pattern,s1):
#     print("找到了")
# else:
#     print("没找到")

# patter = r"^010-\d\d\d\d\d\d\d\d$"
# if re.search(patter,"010-12345678"):
#     print("yes")
# else:
#     print("不是")

# 自己创建原子表   [ows]   [0-9] == \d
# \s == [ \n\t\r]  \w == [0-9a-zA-Z_]
# pattern = r"(19|20)\d\d-(0[1-9]|1[012])-(0[1-9]|1\d|2\d|3[01])"
# print(re.match(pattern,"2019-04-31"))

# 密码验证：3-20，不能是纯数字
# pattern = r"^\w{3}$"
# print(re.match(pattern,"askjefahfasihefa1111"))
# if re.match(r"^\d{3,20}$","1234567891234567890"):
#     print("不能是纯数字")
# print(re.search(pattern,"122kjsdhak"))


# *{0,}
# print(re.search(r"^\d*","p2p0990"))
# + {1,}
# ?name=tom&age=3&key=9
print(re.search(r"^\?(\w+=\w+&?)*","?name=tom&age=3&key=9"))
# print(re.search(r"^\d+","p2p45234"))
# ? {0,1}
# print(re.search(r"^w{3}/?$","www"))
# print(re.search(r"^w{3}/?$","www/"))
# 取消贪婪
# +? 取消贪婪之后只匹配一次
# print(re.match(r'a+?',"aaaaaaaa9"))
# * 贪婪的, *?取消贪婪
# print(re.match(r'a*?',"aaaaaaaa9"))

# 非贪婪
# print(re.match(r'a?',"aaaaaaaa9"))

# 模式修正符
# 正则区分大小写
# re.I 不区分大小写
# print(re.match(r'a+',"aAaddd",re.I))
# re.S 让.匹配任何字符
# print(re.match(r'.+',"\n\n\n",re.S))



# re.M  多行匹配
# print(re.search(r'^a+',"""
# kkkaazzzz
# hellllldd
# aaauuuu
# llllllddd
# """,re.M))






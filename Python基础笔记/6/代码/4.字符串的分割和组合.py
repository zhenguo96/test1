str1 = 'a fox jumped over fox the fence'
# split(seperator) 用指定分隔符分割字符串，返回一个列表
# res = str1.split(" ")
# s2 = "a1b1c"
# print(res, len(res))
# print(s2.split('1'))

# list 可以将字符串转成列表
# a = list(str1)
# print(a)

# partion
# res = str1.partition("over")
# print(res)
#
# s2 = """agc
# bchg
# cih
# dbn
# es
# """
# 按行分割，产生一个数组
# res = s2.splitlines()
# print(res)

# join 将列表的元素用指定分隔符连接为一个字符串
# 要求列表元素必须是字符串
# 分隔符在前
a = ['1','2','3','4']
res = '-'.join(a)
print(res)




# 7.将s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
ls = set(list(s))
ls1 = list(ls)
ls1.sort()
print("".join(ls1))










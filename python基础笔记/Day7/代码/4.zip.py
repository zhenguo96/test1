a = [1,2,3,4]
s1 = "abcdef"
c = (9,8,7,6)
res = zip(a,s1,c)
# print(list(res))
for value in res:
    print(value)

#　=> dict
res = dict(zip(s1,c))
print(res)







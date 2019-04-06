# 增加元素
a = [1,2,3,4]
# append(elem)
# append只能传一个参数，传入的参数会被追加到列表末尾
# a.append(10)
# print(a)
# a.append([15,23])
# print(a)

# extend
# 参数必须是可迭代对象（可以用for in 遍历的对象）
# extend 他会把可迭代对象的元素逐个追加到列表末尾
# a.extend(10)   # 不允许传单个值
# a.extend([10,23,42])
# print(a)

# insert(index, obj)    在指定下标位置插入新的元素，原来的元素后移
# a.insert(0, -9)
# a.insert(0,[9,3,2])
# print(a)

# 其他插入方式
a[:1] = [3, 4, 5, 6 ] # 在指定位置插入多个元素，可能会覆盖原来元素
print(a)
a[len(a):len(a)] = [10, 90, 20]
print(a)
a[1:1] = [30, 40] # 在指定位置插入多个元素，不会覆盖原来元素
print(a)



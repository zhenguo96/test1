#　队列：先进先出
import collections
#
# dq = collections.deque([])
# #右端入队
# dq.append(1)
# dq.append(2)
# dq.append(3)
# print(dq)

# 左端出队
# print(dq.popleft())
# print(dq.popleft())
# print(dq.popleft())

# 约瑟夫环
jose = collections.deque([x for x in range(1,42)])
# print(len(jose))
while len(jose) > 2:
    # 将前两个人加到对尾:
    jose.append(jose.popleft())
    jose.append(jose.popleft())
    # 把第三个人踢出队列
    jose.popleft()
print(jose.popleft())

































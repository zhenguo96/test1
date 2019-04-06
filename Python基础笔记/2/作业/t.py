# 冒泡排序
# def maopao(list):
#     for i in range(len(list) - 1, 0, -1):
#         for j in range(i):
#             if list[j] > list[i]:
#                 list[j],list[i] = list[i], list[j]
# list = [54, 226, 93,17,77,31,44,55,20]
# maopao(list)
# print(list)

# 选择排序
# def xuanze(list):
#     n = len(list)
#     for i in range(n - 1):
#         m = i
#         for j in range(i + 1, n):
#             if list[j] < list[m]:
#                 m = j
#         if m != i:
#             list[i], list[m] = list[m], list[i]
# list = [54, 226, 93,17,77,31,44,55,20]
# xuanze(list)
# print(list)

# 插入排序
# def charu(list):
#     for i in range(len(list) - 1, 0, -1):
#         for j in range(i):
#             if list[j + 1] < list[j]:
#                 list[j + 1], list[j] = list[j], list[j + 1]
# list = [54, 226, 93,17,77,31,44,55,20]
# charu(list)
# print(list)

# 快速排序
def quick_sort(alist, start, end):
    if start >= end:
        return
    mid = alist[start]
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid
    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist, 0, len(alist) - 1)
print(alist)

# 希尔排序
# def shell_sort(alist):
#     n = len(alist)
#     gap = int(n / 2)
#     while gap > 0:
#         for i in range(gap, n):
#             j = i
#             while j >= gap and alist[j - gap] > alist[j]:
#                 alist[j - gap], alist[j] = alist[j], alist[j - gap]
#                 j -= gap
#         gap = int(gap / 2)
# alist = [13, 14, 94, 33, 82, 25, 59, 94, 65]
# shell_sort(alist)
# print(alist)

# 归并排序
# def merge_sort(alist):
#     if len(alist) <= 1:
#         return alist
#     # 二分分解
#     num = int(len(alist) / 2)
#     left = merge_sort(alist[:num])
#     right = merge_sort(alist[num:])
#     # 合并
#     return merge(left, right)
# def merge(left, right):
#     '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
#     # left与right的下标指针
#     l, r = 0, 0
#     result = []
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     result += left[l:]
#     result += right[r:]
#     return result
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# sorted_alist = merge_sort(alist)
# print(sorted_alist)

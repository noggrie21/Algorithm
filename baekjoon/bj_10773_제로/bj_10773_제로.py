import sys
# sys.stdin = open('input.txt')


# def insert(num):
#     global last
#     last += 1
#     stack[last] = num
#     return num
#
#
# def delete():
#     global last
#     result = stack[last]
#     last -= 1
#     return result
#
#
# K = int(input())
# stack = [0] * K
# last = -1
#
# for _ in range(K):
#     num = int(input())
#     if not num:
#         stack[last] = 0
#         last -= 1
#     else:
#         last += 1
#         stack[last] = num
#
# print(sum(stack))

from collections import deque

K = int(input())
stack = deque()

for _ in range(K):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))
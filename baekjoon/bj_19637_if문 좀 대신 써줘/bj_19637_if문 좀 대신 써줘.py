N, M = map(int, input().split())

lookup = [0] * (10**9)
print(lookup)
# n = i = 0
# while n < N:
#     title, upper_limit = map(lambda x: int(x) if x.isdecimal() else x, input().split())
#
#     while i <= upper_limit:
#         lookup.append(title)
#         i += 1
#
#     n += 1
#
# for _ in range(M):
#     index = int(input())
#     print(lookup[index])
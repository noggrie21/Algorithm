# from itertools import combinations
# from functools import reduce
#
# N, M = map(int, input().split())
# S = list(map(int, input().split()))
#
# xyz = list(filter(lambda x: x not in S, range(1, 51)))
#
# candidates = list(map(lambda x: abs(N - reduce(lambda acc, cur: acc * cur, x)), combinations(xyz, 3)))
# # candidates = list(combinations(xyz, M))
#
# print(min(candidates))



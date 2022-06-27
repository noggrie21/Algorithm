# def DFS1(i, r, N, tmp=[]):
#     if i >= r:
#         print(tmp)
#         return
#     else:
#         for j in range(N):
#             if not used[j]:
#                 used[j] = 1
#                 DFS1(i+1, r, N, tmp+[lst[j]])
#                 used[j] = 0
#
#
# # 조합 만들기
# def DFS2(i, r, s, N, temp):
#     if i >= r:
#         print(temp)
#     else:
#         for j in range(s, N):
#             if not used[j]:
#                 used[j] = 1
#                 DFS2(i+1, r, j+1, N, temp+[lst[j]])
#                 used[j] = 0
#
#
# # 부분 집합 만들기
# def DFS3(i, N, temp):
#     if i >= N:
#         print(temp)
#         return
#     DFS3(i+1, N, temp + [lst[i]])
#     DFS3(i+1, N, temp)
#
#
# lst = [6, 7, 8, 9]
# N = len(lst)
# used = [0] * N
# DFS1(0, 3, N)
# # DFS2(0, 3, 0, N, [])
# # DFS3(0, N, [])
#
# # prim 복습



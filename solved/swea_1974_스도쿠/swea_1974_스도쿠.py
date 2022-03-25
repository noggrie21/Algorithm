# import sys
# sys.stdin = open('input (1).txt')
#
# T = int(input())
#
#
# def counting(arr):              # 카운팅 배열을 만들어 1 ~ 9가 모두 1개인지 확인
#     counts = [0] * 10
#     counts_val = 1
#     for i in range(9):          # arr[i] = [7, 3, 6, 4, 2, 9, 5, 8, 1]
#         counts[arr[i]] += 1
#     for j in range(1, 10):      # temp[0]:0이기 때문에 temp[1]부터 순회
#         counts_val *= counts[j]
#     if counts_val == 1:
#         return 1
#     else:
#         return 0
#
#
# for tc in range(1, T+1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
#     result = 1
#
#
#     while True:
#         # 행단위 확인
#         for i in range(9):
#             result *= counting(arr[i])
#             if not result:
#                 break
#
#         # 열단위 확인
#         for i in range(9):
#             temp = []
#             for j in range(9):
#                 temp.append(arr[j][i])
#             result *= counting(temp)
#             if not result:
#                 break
#
#         # 사각형 단위 확인
#         di = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
#         dj = [-1, 0, 1, 1, 1, 0, -1, -1, 0]
#         for i in range(1, 9, 3):
#             temp = []
#             for j in range(1, 9, 3):
#                 for k in range(9):
#                     ni = i + di[k]
#                     nj = j + dj[k]
#                     temp.append(arr[ni][nj])
#                 result *= counting(temp)
#                 if not result:
#                     break
#         break
#
#     print(f'#{tc} {result}')










    # # 행 확인
    # for i in range(9):
    #     total = 0
    #     counts_r = [0] * 10
    #     for j in range(9):
    #         counts_r[arr[i][j]] = 1
    #     for count in counts_r:
    #         total += count
    #     if total == 9:
    #         result *= 1
    #     else:
    #         result *= 0
    #
    # # 열 확인
    # for i in range(9):
    #     total = 0
    #     counts_c = [0] * 10
    #     for j in range(9):
    #         counts_c[arr[j][i]] = 1
    #     for count in counts_c:
    #         total += count
    #     if total == 9:
    #         result *= 1
    #     else:
    #         result *= 0
    #
    # # 사각형 확인
    # for i in range(1, 9, 3):
    #     total = 0
    #     counts_b = [0] * 10
    #     for j in range(1, 9, 3):
    #         for k in range(9):
    #             ni = di[k] + i
    #             nj = dj[k] + j
    #             counts_b[arr[ni][nj]] = 1
    #     for count in counts_b:
    #         total += count
    #     if total == 9:
    #         result *= 1
    #     else:
    #         result *= 0

    # print(f'#{tc}', arr)

    # if (i % 3) * (j % 3) == 1:
    #     for k in range(9):
    #         ni = di[k] + i
    #         nj = dj[k] + j
    #         if 0 <= ni < 9 and 0 <= nj < 9:
    #             counts_b[arr[ni][nj]] = 1
    #
    # for idx in range(9):
    #     if not counts_r[idx]*counts_c[idx]*counts_b[idx]:
    #         print(f'{tc} 0')
    #         break
    # else:
    #     print(f'{tc} 1')
    #
    #
    # for count in counts:
    #     total += count
    # if total == 9:
    #     result *= 1
    # else:
    #     result *= 0
    #
    # # 열 확인
    # counts = [0] * 10
    # for i in range(9):
    #     for j in range(9):
    #         counts[arr[j][i]] = 1
    # for count in counts:
    #     total += count
    # if total == 9:
    #     result *= 1
    # else:
    #     result *= 0
    #
    # # 사각형 확인
    # counts = [0] * 10
    #

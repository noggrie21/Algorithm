import sys
sys.stdin = open('input.txt')


def cnt_palindrome(arr):
    if arr == arr[::-1]:
        return len(arr)
    else:
        return 0


for x in range(10):
    tc = int(input())
    matrix = [list(input()) for _ in range(100)]
    max_cnt = 1

    # 행방향 탐색
    for i in range(100):
        for j in range(100):
            for k in range(j + 1, 100):
                if matrix[i][j] == matrix[i][k]:
                    cnt = cnt_palindrome(matrix[i][j:k + 1])
                    if max_cnt < cnt:
                        max_cnt = cnt

    # 열방향 탐색
    for i in range(100):
        for j in range(100):
            for k in range(j + 1, 100):
                if matrix[j][i] == matrix[k][i]:
                    temp = ''
                    for l in range(j, k+1):
                        temp += matrix[l][i]
                    cnt = cnt_palindrome(temp)
                    if max_cnt < cnt:
                        max_cnt = cnt
    print(f'#{tc} {max_cnt}')





    # # def max_palindrome(arr):
    #     max_cnt = 0
    #     for i in range(100):
    #         for j in range(100):
    #             # temp = []
    #             for k in range(j + 1, 100):
    #                 if arr[i][j] == arr[i][k]:
    #                     # temp = matrix[i][j:k+1]
    #                     cnt = cnt_palindrome(arr[i][j:k + 1])
    #                     if max_cnt < cnt:
    #                         max_cnt = cnt
    #     # return max_cnt



    # for i in range(100):
    #     for j in range(100):
    #         if i < j:
    #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    #
    # transpose = cnt_palindrome(matrix)
    #
    # if origin < transpose:
    #     print(f'#{tc} {transpose}')
    # else:
    #     print(f'#{tc} {origin}')

    # for i in range(100):
    #     for j in range(100):
    #         # temp = []
    #         for k in range(j + 1, 100):
    #             if matrix[j][i] == matrix[k][i]:
    #                 temp = ''
    #                 for l in (j, k+1):
    #                     temp += matrix[l][i]
    #                 # temp = matrix[i][j:k+1]
    #                 cnt = cnt_palindrome(temp)
    #                 if max_cnt < cnt:
    #                     max_cnt = cnt
    # print(max_cnt)
                #
                # for i in range(100):
                #     for j in range(100):
                #         temp = []
                #         for k in range(j + 1, 100):
                #             if matrix[i][j] == matrix[i][k]:
                #                 temp = matrix[i][j:k + 1]
                #                 cnt = cnt_palindrome(temp)
                #                 if max_cnt < cnt:
                #                     max_cnt = cnt
                # if matrix[j][i] == matrix[k][i]:
                #     temp = matrix[i][j:k+1]
                #     cnt = cnt_palindrome(temp)
                #     if max_cnt < cnt:
                #         max_cnt = cnt


    # print(matrix[0][2:8])
    # print()
    # print(matrix[0][2:9])
    # print(matrix[0][0:5]) ['C', 'C', 'B', 'B', 'C']

    # result = list(filter(None, result))
    # print(f'#{tc}', ' '.join(result))
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# for tc in range(1, T+1):
#     board = [[0]*10 for _ in range(10)]
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     for i in range(N):
#         # print(arr[i])
#         for j in range(arr[i][2]-arr[i][0]+1):
#             for k in range(arr[i][3]-arr[i][1]+1):
#                 board[arr[i][0]+j][arr[i][1]+k] += arr[i][4] #
#     # print(board)
#     purple = 0
#     for l in range(10):
#         for m in range(10):
#             if board[l][m] == 3:
#                 purple += 1
#     print(f'#{tc} {purple}')

for tc in range(1, T + 1):
    board = [[0] * 10 for _ in range(10)]
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    purple = 0
    for i in range(N):
        # print(arr[i])
        for j in range(arr[i][2] - arr[i][0] + 1):
            for k in range(arr[i][3] - arr[i][1] + 1):
                board[arr[i][0] + j][arr[i][1] + k] += arr[i][4]  #
                if [arr[i][0] + j][arr[i][1] + k] == 3:
                    purple += 1
    print(f'#{tc} {purple}')
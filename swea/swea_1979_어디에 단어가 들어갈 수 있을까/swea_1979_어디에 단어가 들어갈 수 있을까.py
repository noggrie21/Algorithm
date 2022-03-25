

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    result = 0

    # 가로행을 탐색한다고 했을 경우,
    # 하나씩 순회할 때(puzzle[i][j]) 한번에 옆칸, 옆옆칸, 옆옆옆칸까지(K = 3여서) 모두 1인지 확인하고
    # 그 한 세트의 양 옆(puzzle[i][j-1]과 puzzle[i][j+K])이 모두 0인 경우에 result에 +1 추가
    # puzzle[i][0]이나 puzzle[N-1][j]처럼 제일 사이드의 경우 IndexError가 날 수 있기 때문에,
    # 입력받을때 2차원배열을 0으로 둘러싼 형태로 입력받음

    for i in range(1, N + 1):                       # 행 찾기
        for j in range(1, N-K+2):
            temp = []
            for k in range(K):
                temp.append(puzzle[i][j+k])
            if 0 not in temp:
                if puzzle[i][j - 1] + puzzle[i][j + K] == 0:
                    result += 1

    for i in range(1, N + 1):                        # 열 찾기
        for j in range(1, N - K + 2):
            temp = []
            for k in range(K):
                temp.append(puzzle[j + k][i])
            if 0 not in temp:
                if puzzle[j - 1][i] + puzzle[j + K][i] == 0:
                    result += 1

    print(f'#{tc} {result}')






            # if puzzle[i][j] & puzzle[i][j+1] & puzzle[i][j+2]:
            #     if puzzle[i][j-1] + puzzle[i][j+3] == 0:
            #         result += 1





    #
    #              cnt = 1
    #             nj = j + 1
    #             while 0 <= nj < N:
    #                 if not puzzle[i][nj]:
    #                    break
    #                 cnt += 1
    #                 nj += 1
    #             if cnt == K:
    #                 result += 1
    #             break
    #
    # # 열 확인
    # for i in range(N):
    #     for j in range(N):
    #         if puzzle[j][i]:
    #             cnt = 1
    #             nj = j + 1
    #             while 0 <= nj < N:
    #                 if not puzzle[nj][i]:
    #                    break
    #                 cnt += 1
    #                 nj += 1
    #             if cnt == K:
    #                 result += 1
    #                 break
    # print(result)
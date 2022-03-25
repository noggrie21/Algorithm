'''
보드는 4x4, 6x6, 8x8
돌을 놓을 수 있는 곳 규칙 잘 보기...근데 BFS인듯

 N은 4, 6, 8 중 하나
 (보드의 한 변의 길이 N)
 플레이어가 돌을 놓는 횟수 M

 1이면 흑돌, 2이면 백돌
 3 2 1이 입력된다면 (3, 2) 위치에 흑돌

 출력: 흑돌, 백돌의 개수
'''

import sys
sys.stdin = open('sample_input(1).txt')


T = int(input())
di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]


# DFS인자(i, j, lst(다른 돌을 만났을 때 해당 위치 정보 기록), k(델타배열 인덱스), color(색 정보))
def DFS(i, j, lst, k, color):
    if board[i][j] == color:       # 같은 돌을 만나면 함수 종료
        for r, c in lst:           # 위치 정보를 하나씩 빼서
            board[r][c] = color    # 현재 색 바꿔주기
        return
    elif not board[i][j]:          # 또는 빈 공간 또는 벽을 만나면
        return                     # 함수 종료
    DFS(i+di[k], j+dj[k], lst+[(i, j)], k, color) # 다른 돌을 만나면 다음 함수를 호출하고, 위치 정보 업데이트하기


# 흰 돌과 검은 돌을 세주는 함수(처음에 검은 돌만 세고, N**2에서 빼주는 식으로 했다가 오지게 fail 당함...)
def count_color():
    white = black = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    return black, white


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # N * N 배열을 0으로 둘러싸서 인덱스도 맞추고, 델타에 따른 유효성 검사 패스..
    board = [[0] * (N + 2)] + [[0] + [0] * N + [0] for _ in range(N)] + [[0] * (N + 2)]

    # 돌 초기 세팅하기
    n = N // 2
    board[n][n+1] = board[n+1][n] = 1
    board[n][n] = board[n+1][n+1] = 2

    for _ in range(M):
        i, j, color = map(int, input().split())
        board[i][j] = color
        for k in range(8):
            DFS(i+di[k], j+dj[k], [], k, color)     # 놓은 돌의 주변부 탐색

    print(f'#{tc}', *count_color())
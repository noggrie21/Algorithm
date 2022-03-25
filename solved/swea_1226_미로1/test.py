import sys
sys.stdin = open('input (1).txt')

T = 10

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(start_row, start_col, end_row, end_col):
    for i in range(4):
        if arr[end_row][end_col] == 1:
            return
        if arr[start_row + dy[i]][start_col + dx[i]] != 1:
            arr[start_row + dy[i]][start_col + dx[i]] = 1
            dfs(start_row + dy[i], start_col + dx[i], end_row, end_col)


for dum in range(T):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    start = [None, None]
    end = [None, None]

    for i in range(16):
        if 2 in arr[i]:
            for j in range(16):
                if 2 == arr[i][j]:
                    start[0], start[1] = i, j
        if 3 in arr[i]:
            for j in range(16):
                if 3 == arr[i][j]:
                    end[0], end[1] = i, j

    dfs(start[0], start[1], end[0], end[1])
    if arr[end[0]][end[1]] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
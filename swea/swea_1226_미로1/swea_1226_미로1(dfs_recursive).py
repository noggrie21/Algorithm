import sys
sys.stdin = open('input (1).txt')


def findstart(array):               # 시작점 찾기
    for i in range(16):
        for j in range(16):
            if array[i][j] == 2:
                return i, j


def dfs(i, j):
    global result
    if array[i][j] == 3:
        result = 1
        return
    array[i][j] = 1
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if array[ni][nj] != 1:
            dfs(ni, nj)


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for t in range(1, 11):
    tc = int(input())
    array = [list(map(int, input())) for _ in range(16)]
    sti, stj = findstart(array)
    result = 0
    dfs(sti, stj)
    print(f'#{tc} {result}')


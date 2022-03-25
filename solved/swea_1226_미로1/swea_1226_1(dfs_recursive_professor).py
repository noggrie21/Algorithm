import sys
sys.stdin = open('input (1).txt')


def findstart(array):               # 시작점 찾기
    for i in range(16):
        for j in range(16):
            if array[i][j] == 2:
                return i, j


def dfs(i, j):
    if array[i][j] == 3:
        return 1
    else:
        array[i][j] = 1
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if array[ni][nj] != 1:
               if dfs(ni, nj):
                   return 1
    return 0


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for t in range(1, 11):
    tc = int(input())
    array = [list(map(int, input())) for _ in range(16)]
    sti, stj = findstart(array)
    result = 0
    dfs(sti, stj)
    print(f'#{tc} {dfs(sti, stj)}')


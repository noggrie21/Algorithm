import sys
sys.stdin = open('input (1).txt')


def findstart(array):               # 시작점 찾기
    for i in range(16):
        for j in range(16):
            if array[i][j] == 2:
                return i, j


def dfs(i, j, distance):
    global minV
    if array[i][j] == 3:

        return
    else:
        array[i][j] = 1
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if array[ni][nj] != 1:
                dfs(ni, nj, distance + 1)
                
        array[i][j] = 0


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for t in range(1, 11):
    tc = int(input())
    array = [list(map(int, input())) for _ in range(16)]
    sti, stj = findstart(array)
    distance = 0
    minV = 16 * 16
    dfs(sti, stj, distance)
    print(f'#{tc} {distance}')


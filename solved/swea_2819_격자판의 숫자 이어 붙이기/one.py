import sys
sys.stdin = open('sample_input.txt')

T = int(input())

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def DFS(i, j, lst):
    global results
    lst = lst + [board[i][j]]
    if len(lst) == 7:
        if lst not in results:
            results.append(lst)
        return
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            DFS(ni, nj, lst)


for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    results = []

    for r in range(4):
        for c in range(4):
            DFS(r, c, [])

    print(f'#{tc} {len(results)}')
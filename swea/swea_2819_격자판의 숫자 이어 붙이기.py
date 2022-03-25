# 격자판: 4*4
# 격자판에는 0 ~ 9 숫자 적힘
# 임의의 위치에서 시작
# 6번 이동(동서남북) 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 됨
import sys
sys.stdin = open('sample_input.txt')


# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

T = int(input())


def DFS(i, j, lst):
    global results
    if len(lst) == 7:
        number = ''.join(map(str, lst))
        results.add(number)
        return
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            DFS(ni, nj, lst + [board[i][j]])


for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    results = set()

    for r in range(4):
        for c in range(4):
            DFS(r, c, [])

    print(f'#{tc} {len(results)}')



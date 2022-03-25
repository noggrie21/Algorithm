import sys
sys.stdin = open('input (1).txt')

for _ in range(10):
    tc = input()
    data = [list(map(int, input().split())) for _ in range(100)]
    move = [[0]*100 for _ in range(100)]
    i = 99
    j = k = 0
    # 좌, 우, 상 순으로 확인하는 델타
    di = [0, 0, -1]
    dj = [-1, 1, 0]

    for a in range(100): # a: 도착점의 열값
        if data[99][a] == 2:
            j = a
            break

    while True:
        if not i:
            break
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 100 and 0 <= nj < 100:
            if not data[ni][nj]:
                k += 1
            else:
                if not move[ni][nj]:
                    i, j = ni, nj
                    move[i][j] = 1
                    k = 0
                else:
                    k += 1
        else:
            k += 1

    print(f'#{tc} {j}')

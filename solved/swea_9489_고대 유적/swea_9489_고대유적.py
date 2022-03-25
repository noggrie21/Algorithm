import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    cnt = 0


    # N과 M이 다를 경우에는
    # 이중 for문을 돌 때
    # 행과 열의 범위 위치를 바꿔줘야 함

    # 행탐색
    for i in range(N):
        for j in range(M):
            if under[i][j] == 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0
        cnt = 0

    # 열탐색
    for j in range(M):
        for i in range(N):
            if under[i][j] == 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0
        cnt = 0

    print(f'#{tc} {max_cnt}')
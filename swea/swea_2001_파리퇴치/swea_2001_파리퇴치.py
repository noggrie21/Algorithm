import sys
sys.stdin = open('input (1).txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_catch = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for k in range(M):
                for l in range(M):
                    catch += flies[i+k][j+l]
            if max_catch < catch:
                max_catch = catch
    print(f'#{tc} {max_catch}')


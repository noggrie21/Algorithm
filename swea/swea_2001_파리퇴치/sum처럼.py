import sys
sys.stdin = open('input (1).txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum1 = sum2 = 0                     # 대각선과 반대 대각선의 합 초기화
            for k in range(M):
                sum3 = sum4 = 0                 # 행과 열의 합 초기화
                sum1 += flies[i+k][j+k]         # sum1 : 대각선의 합
                sum2 += flies[i+k][j+M-1-k]     # sum2 : 반대대각선의 합
                for l in range(M):
                    sum3 += flies[i+k][j+l]     # sum3 : 행의 합
                    sum4 += flies[i+l][j+k]     # sum4 : 열의 합
                if maxV < sum1:                 # 최댓값 구하기
                    maxV = sum1
                if maxV < sum2:
                    maxV = sum2
                if maxV < sum3:
                    maxV = sum3
                if maxV < sum4:
                    maxV = sum4
    print(f'{tc} {maxV}')


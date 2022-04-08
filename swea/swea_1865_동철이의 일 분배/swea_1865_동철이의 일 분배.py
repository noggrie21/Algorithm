import sys
sys.stdin = open('input (1).txt', 'r')

T = int(input())


def probability(a):                         # 입력값 확률로 변환하는 함수
    return float(a)/100


def DFS(i, total):
    global ans

    # 가지치기
    if not total or total < ans:             # total에 0이 곱해진 순간 어떤 수를 곱하든 0이 되기 때문에 탐색 종료
        return

    # 기저 파트
    elif i >= N:                               # 모두 일을 배분 받았다면
        if ans < total:                      # 갱신할 수 있는 값인지 확인
            ans = total
        return

    # 유도 파트
    else:
        for j in range(N):
            if not assign[j]:
                assign[j] = True
                DFS(i+1, total*p[i][j])
                assign[j] = False


for tc in range(1, T+1):
    N = int(input())
    p = [list(map(probability, input().split())) for _ in range(N)]
    ans = 0
    assign = [False] * N
    print(f'#{tc} {ans*100:6f}')

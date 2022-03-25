import sys
sys.stdin = open('sample_in.txt')


def check(bustype, A, B):
    global stop
    stop[A] += 1
    stop[B] += 1
    if bustype == 1:                      # 일반버스 일때
        for i in range(A + 1, B):
            stop[i] += 1
    elif bustype == 2:                    # 급행버스 일때
        for j in range(A + 2, B, 2):
            stop[j] += 1
    else:
        for k in range(A + 1, B):         # 광역 급행버스일 때
            if A % 2:                     # A가 홀수일 때
                if not k % 3 and k % 10:
                    stop[k] += 1
            else:                         # A가 짝수일 때
                if not k % 4:
                    stop[k] += 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    stop = [0] * 1001
    for _ in range(N):
        bustype, A, B = map(int, input().split())
        check(bustype, A, B)
    stop = list(filter(None, stop))
    max_cnt = 1
    for cnt in stop:
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')
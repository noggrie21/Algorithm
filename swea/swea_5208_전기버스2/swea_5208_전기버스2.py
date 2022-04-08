import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def recur(num, end, cnt):                       # num: 현재 정류장 / end: 종점 / cnt: 이동 횟수
    global ans

    # 가지치기
    if ans < cnt:                               # 이동 횟수가 ans보다 크면
        return                                  # 탐색 종료

    # 기저파트
    if num >= end:                              # 현재 정류장이 종점보다 크면
        cnt -= 1                                # 종착점을 제외하고 몇 개의 정류장을 거쳤는지 출력해야 하기 때문에 현재 이동 횟수 -1
        ans = min(ans, cnt)                     # ans와 cnt중 최솟값으로 ans 갱신

    # 유도파트
    else:
        for i in range(arr[num], 0, -1):        # 현재 위치에서 가장 멀리갈 수 있는 곳부터
            recur(num+i, end, cnt+1)            # 가보기!


for tc in range(1, T+1):
    N, *arr = map(int, input().split())         # N = 5 / arr = [2, 3, 1, 1] 형태로 입력받기
    arr = [0] + arr                             # 정류장 번호와 인덱스 일치시켜주기 위해 패딩값 0 앞에 넣어주기
    ans = N                                     # 정류장 수로 초기화
    recur(1, N, 0)                              # 출발점, 종점(=정류장 수), 이동 횟수 인자로 넘겨주기
    print(f'#{tc} {ans}')

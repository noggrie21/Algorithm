import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def binary_search(start, end, key):
    old = 2                             # old: 이전 탐색 방향을 기록용 (초기화: 왼쪽, 오른쪽과 다른 값)

    while start <= end:
        middle = (start + end) // 2

        if a[middle] == key:            # key 찾으면
            return 1                    # 1을 반환

        elif a[middle] > key:           # 왼쪽 탐색을 해야하는 경우에

            if not old ^ 0:             # 이전 탐색 방향과 같으면
                return                  # 탐색 종료
            else:                       # 다르면,
                end = middle - 1        # end 조정
                old = 0                 # 방향 왼쪽(0)으로 기록

        else:                           # 오른쪽 탐색을 해야하는 경우에

            if not old ^ 1:             # 이전 탐색 방향 같으면
                return                  # 탐색 종료
            else:                       # 다르면,
                start = middle + 1      # start 조정
                old = 1                 # 방향 오른쪽(1)으로 기록


for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    cnt = 0

    for key in b:
        if binary_search(0, N-1, key):
            cnt += 1

    print(f'#{tc} {cnt}')
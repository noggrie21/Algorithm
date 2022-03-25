import sys
sys.stdin = open('sum_input (1).txt')


# 델타를 사용하여 우, 하, 좌, 상으로 움직이되
# 가장자리의 합이라 함은 각 위치가 1번씩만 더해진 값이기 때문에
# 이동한 위치를 기록하여 이미 이동한 적이 있는 좌표가 나올때 합산을 멈춘다.

for _ in range(10):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    di = [0, 1, 0, -1]                              # 델타배열 : 우, 하, 좌, 상
    dj = [1, 0, -1, 0]
    load = []                                       # 이동한 위치를 기록하는 리스트
    i = j = k = 0
    total = arr[0][0]                               # 맨 앞값으로 초기화
    while True:
        load.append((i, j))                         # 현재 위치를 기록
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 100 and 0 <= nj < 100:         # 유효한 범위인지 확인
            if (ni, nj) not in load:                # 이동한 적이 없는지 확인
                i = ni                              # i 갱신
                j = nj                              # j 갱신
                total += arr[i][j]
            else:                                   # 이동한 적이 있다면 반복문 탈출
                break
        else:                                       # 유효한 범위가 아니면 델타를 다른 방향으로 전환
            k += 1
    print(f'#{tc} {total}')


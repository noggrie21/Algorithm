import sys
sys.stdin = open('input (1).txt')


# 출력 : 처음 출발해야할 방 번호, 최대 몇 개의 방을 이동할 수 있는 지(겹치면 작은 방 번호 뽑기)
# 1 <= A[i][j] <= N**2 (A[i][j]는 모두 다른 수)
# 이동 방향 :  상하좌우
# 이동 조건 : 1. 방이 존재 2. 현재 방 + 1 = 이동하려는 방


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    room_arr = [[-1, -1] for _ in range(n * n + 2)]  # 방 번호 배열, 앞 뒤로 패딩을 넣어준다.(앞 패딩은 방번호가 1부터 시작)
    print(arr)

    for i in range(n):  # 방 번호를 인덱스로 하는 배열 / 해당 값의 [0] : 방 번호의 i의 좌표 / 해당 값의 [1] : 방 번호의 j 좌표
        for j in range(n):
            room_arr[arr[i][j]] = [i, j]
    print(room_arr)

    room = 0  # 방 번호
    max_cnt = 0  # 이동 횟수
    cnt = 1  # 현재 이동 횟수
    for i in range(1, n * n + 1):  # i: 방번호 / 마지막까지 차이가 1이면 max_cnt를 확인하지 않으니, 끝에 패딩을 넣어준 것까지 비교한다.
        if abs(room_arr[i][0] - room_arr[i + 1][0]) + abs(room_arr[i][1] - room_arr[i + 1][1]) == 1:
            if cnt == 1:  # 시작점 표시
                start = i
            cnt += 1
        else:
            if max_cnt < cnt:  # 이동 횟수가 더 클 때
                max_cnt = cnt
                room = start
            cnt = 1

    print(f'#{tc} {room} {max_cnt}')
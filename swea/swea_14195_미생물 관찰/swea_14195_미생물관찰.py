import sys
sys.stdin = open('sampleinput.txt')


T = int(input())


def switch(char): # switch: A -> 1 / B -> 2 / _ -> 0
    if char == 'A':
        return 1
    elif char == 'B':
        return 2
    else:
        return 0


def BFS(si, sj, types):                                                     # (si, sj):시작위치 / types: 미생물 타입
    queue = [(si, sj)]
    sample[si][sj] = 0
    cnt = 1                                                                 # 시작 위치부터 크기 1이기 때문에 1로 초기화

    while queue:
        i, j = queue.pop(0)
                                                                            # 현재 위치 빈공간으로 바꾸
        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and sample[ni][nj] == types:     # 미생물 타입이 같으면 queue에 추가
                queue.append((ni, nj))                                      # queue에 삽입하면서
                cnt += 1                                                    # 크기 +1 해주고
                sample[ni][nj] = 0                                          # 카운트 된 부분이면 다시 추가되지 않도록 빈공간으로 갱신해주기

    return cnt, types


for tc in range(1, T+1):
    N, M = map(int, input().split())
    sample = [list(map(switch, input())) for _ in range(N)]

    maxV = 0                                                                # maxV: 가장 큰 개체의 크기
    cnt_a = 0                                                               # cnt_a: a 타입의 개체 수
    cnt_b = 0                                                               # cnt_b: b 타입의 개체 수

    for i in range(N):
        for j in range(M):
            if sample[i][j]:                                                # 1(A) 또는 2(B)일 때 즉, 미생물일 때
                cnt, types = BFS(i, j, sample[i][j])                        # BFS에 해당 위치와 타입을 인자로 넘기고, 개체의 크기와 타입을 반환받는다.

                if types == 1:                                              # 1(A) 타입인 경우,
                    cnt_a += 1                                              # cnt_a += 1
                else:                                                       # 2(B) 타입인 경우,
                    cnt_b += 1                                              # cnt_b += 1

                if maxV < cnt:                                              # 개체 크기가 기존의 개체 크기보다 큰 경우
                    maxV = cnt                                              # maxV 갱신

    print(f'#{tc} {cnt_a} {cnt_b} {maxV}')
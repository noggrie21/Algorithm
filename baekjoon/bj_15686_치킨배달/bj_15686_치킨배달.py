def search_coordinate():
    chicken = []
    house = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 2:
                chicken.append((i, j))
            elif city[i][j] == 1:
                house.append((i, j))
    return chicken, house


# n개의 숫자에서 r 자릿 수 만들기
def nCr(s, r, idx, N): # s: 현재 자릿 수 / r: 총 자릿 수 / idx: 고를 수 있는 구간의 시작 인덱스/ N: 주어진 수의 갯수
    global ans

    # 기저 파트
    if s >= r: # 치킨집 조합이 정해졌을 때,
        minD = [10000]*len(house) # 가정집마다 치킨 거리가 담길 배열
        for i in range(N):
            if used[i]:
                for idx in range(len(house)):
                    distance = abs(chicken[i][0] - house[idx][0]) + abs(chicken[i][1] - house[idx][1])
                    minD[idx] = min(distance, minD[idx])
        ans = min(ans, sum(minD))
        return

    # 유도 파트
    else:
        for i in range(idx, N):
            if not used[i]:
                used[i] = 1
                nCr(s+1, r, i+1, N)
                used[i] = 0


import sys
N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 치킨집과 가정집 좌표 구하기
chicken, house = search_coordinate()

# 치킨집 조합 구하기
used = [0] * len(chicken)
ans = 100000
nCr(0, M, 0, len(chicken))

print(ans)


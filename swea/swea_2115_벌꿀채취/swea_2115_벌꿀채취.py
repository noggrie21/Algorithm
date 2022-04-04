import sys
sys.stdin = open('sample_input.txt', 'r')
'''
3 <= N <= 10
1 <= M <= 5 (M<=N, M은 반드시 N 이하)
10 <= C <= 30
1 <= 한 벌통에 들어있는 꿀 양 <= 9

'''
revenue = [0] * 10                                                  # revenue = [0, 1, 4, 9, 16, ...]
for idx in range(10):
    revenue[idx] = idx**2

def DFS(n, N, ssum, temp, arr):
    global sol

    # 가지치기
    if sum(temp) > C:
        return

    # 기저 파트
    if n >= N:
        sol = max(sol, ssum)
        return

    # 유도 파트
    else:
        DFS(n+1, N, ssum, temp, arr)
        DFS(n+1, N, ssum + revenue[arr[n]], temp+[arr[n]], arr)


def search_maxR():
    global ans
    global sol

    spot = (-1, -1)
    result = 0

    for i in range(N):
        for j in range(N-M+1):
            if 0 in beehive[i][j:j+M]:                              # 꿀이 없는 벌통이 포함되어 있는 경우
                continue                                            # 건너뛰기

            total = 0                                               # 수익이 담길 변수

            if sum(beehive[i][j:j+M]) <= C:                         # C의 양을 넘어서지 않으면
                for honey in beehive[i][j:j+M]:                     # 하나씩 수익 계산
                    total += revenue[honey]                         # total에 반영

            else:
                sol = 0                                             # C의 양을 넘어서면
                DFS(0, M, 0, [], beehive[i][j:j+M])                 # 가능한 가장 큰 수익이 되는 경우 DFS로 구하기
                total = sol

            if total > result:                                      # total이 기존 result보다 큰 경우
                spot = (i, j)                                       # 벌통 위치 기록
                result = total                                      # result 갱신

    ans += result
    return spot


T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())                             # N: 벌통들의 크기, M: 선택할 수 있는 벌통의 크기, C: 채취할 수 있는 최대 양
    beehive = [list(map(int, input().split())) for _ in range(N)]
    ans = 0                                                         # 두 일꾼이 꿀을 채취하여 얻을 수 있는 최대 수익
    sol = 0
    spot = search_maxR()                                            # 최대 수익 ans에 더해주고, 해당 벌통 시작 위치 반환값으로 받기
    beehive[spot[0]][spot[1]:spot[1]+M] = [0] * M                   # 최대 수익이 난 벌통 꿀 다 빼버리기
    spot = search_maxR()                                            # 그 다음 최대 수익을 ans에 더해주기(벌통 위치를 반환값으로 받지만 따로 활용하지 않음)
    print(f'#{tc} {ans}')
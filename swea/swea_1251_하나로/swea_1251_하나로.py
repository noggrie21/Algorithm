import sys
sys.stdin = open('input (1).txt')


T = int(input())


def MST(s):
    global tc
    mst = [-1] * N                                                          # mst에 등록 여부와 노드번호를 인덱스로 하여 해당 노드로 가기 위한 최소 비용이 값으로 담길 예정
    mst[s] = 0                                                              # 시작 정점의 비용은 0
    ans = 0

    # 초기 값이 들어있지 않을 때까지(=모든 정점이 mst에 등록될 때까지) 반복
    while -1 in mst:
        minV = 2*10**12+1                                                     # 비용의 최댓값보다 큰 수로 초기화
        node = -1                                                           # 인덱스로 나오지 않는 수로 초기화

        # mst에 등록된 노드와 인접한 노드 중에서
        for rn in range(N):
            if -1 < mst[rn]:

                # mst에 미등록 되어있으며 최소 비용을 가진 노드 찾기
                for urn in range(N):
                    if mst[urn] < 0 and adjM[rn][urn] < minV:
                        minV = adjM[rn][urn]
                        node = urn

        # mst에 등록하기
        mst[node] = 1
        ans += minV
    return int(E*ans+0.5)


for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    adjM = [[0]*N for _ in range(N)]                                        # 인접 행렬 리스트 초기화

    for i in range(N):                                                      # 무방향 그래프이기 때문에 i < j구간만 순회해도 모든 정점에 대한 가중치 기록 가능
        for j in range(i+1, N):
            adjM[i][j] = adjM[j][i] = (X[i]-X[j])**2 + (Y[i]-Y[j])**2       # 비용은 L**2이기 때문에 (x좌표의 차)**2+(y좌표의 차)**2

    ans = MST(0)                                                            # 0번 정점에서 시작(어떤 정점으로 시작해도 같음)
    print(f'#{tc} {ans}')


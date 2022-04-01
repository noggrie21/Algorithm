# MST 만들기(인접 행렬 리스트 사용)

def mst_prim(G, s): # G: 무방향 그래프, s: 시작 정점
    '''
    1. 임의의 (시작)정점 선택
    2. 선택한 정점과 연결된 정점(MST에 등록되지 않은 정점)들을 순회하면서 작은 가중치를 갖는 정점 선택
    2. mst에 등록
    3. mst에 모든 정점이 등록될 때까지 혹은 정점 갯수 -1 만큼(시작 정점은 제외) 반복하기
    '''

    used = [-1] * (V + 1)                                       # used: mst 등록 여부 배열 / 초기값 -1 / 갱신 시 used[idx] = idx번 정점과 MST에 등록된 인접 정점과의 최소 가중치
    used[s] = 0                                                 # 시작 정점 MST에 등록
    ans = 0

    while -1 in used:                                           # MST에 모든 정점이 등록될 때까지 순회

        # 초기화
        minV = initial                                          # 가중치로 나올 수 없는 큰 수
        idx = -1                                                # 정점 번호가 아닌 수

        # MST에 등록된 정점 찾기
        for v in range(V + 1):
            if 0 <= used[v]:                                    # 초기값이 음수이므로 0 <= used[v]면, v는 등록된 정점

                # 새로 등록할 정점 찾기
                for nv in range(V + 1):
                    if used[nv] < 0 and 0 < G[v][nv] < minV:    # MST 미등록 정점이면서,  자기 자신이 아니고 최소 가중치
                        minV = G[v][nv]
                        idx = nv

        used[idx] = minV                                        # used[idx] 갱신하기

    ans = sum(used)                                             # used = [0, 21, 31, 34, 46, 18, 25]
    return ans


V, E = map(int, input().split())                                # V: 마지막 정점의 번호, E: 간선의 갯수

# 인접 행렬 리스트 만들기
initial = 10000
adj = [[initial] * (V + 1) for _ in range(V + 1)]

# 인접 행렬 리스트에 가중치 입력받기
for _ in range(E):
    v1, v2, w = map(int, input().split())
    adj[v1][v1] = adj[v2][v2] = 0
    adj[v1][v2] = adj[v2][v1] = w                               # 최소 신장 트리는 무방향 그래프에 N개의 정점을 N-1개의 간선을 연결한 최소비용

print(mst_prim(adj, 0))                                                # 무방향 그래프와 시작 정점 인자로 넘겨주기
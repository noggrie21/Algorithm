import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def mst_prim(G, s):
    # used: mst 등록 여부 배열
    # 초기값 -1
    # 갱신 시 used[idx] = idx번 정점과 MST에 등록된 인접 정점과의 최소 가중치
    used = [False] * (V + 1)
    used[s] = True  # 시작 정점 MST에 등록
    ans = 0

    while V:  # MST에 모든 정점이 등록될 때까지 순회

        # 초기화
        minV = initial  # 가중치로 나올 수 없는 큰 수
        idx = -1  # 정점 번호가 아닌 수

        for v in range(V + 1):  # MST에 등록된 정점 순회하기
            if 0 <= used[v]:  # (초기값이 음수이므로, 0 이상 = 등록된 정점)

                for nv in range(V + 1):  # 새로 등록할 정점 찾기
                    if used[nv] < 0 and 0 < G[v][nv] < minV:  # MST 미등록 정점 and 자기 자신이 아니면서 최소 가중치
                        minV = G[v][nv]
                        idx = nv

        used[idx] = True  # used[idx] 갱신하기
        ans += minV
    ans = sum(used)  # used = [0, 21, 31, 34, 46, 18, 25]
    return ans


for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*V for _ in range(V)]

    initial = 10000
    adj = [[initial] * (V + 1) for _ in range(V + 1)]

    # 인접 행렬 리스트에 가중치 입력받기
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        adj[v1][v2] = adj[v2][v1] = w  # 최소 신장 트리는 무방향 그래프에 N개의 정점을 N-1개의 간선을 연결한 최소비용

    print(f'#{tc} {mst_prim(adj, 0)}')  # 무방향 그래프와 시작 정점 인자로 넘겨주기
def BFS(v):
    q = [v]
    tree = [0] * (N+1)
    tree[v] = -1

    while q:
        parent = q.pop(0)
        print(graph, parent, graph[parent])
        for node in graph[parent]:
            if not tree[node]:
                tree[node] = parent

    return tree


N = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]


for _ in range(N-1):
    v1, v2 = map(int, input().split())
    graph[v1] = v2
    graph[v2] = v1

tree = BFS(1)
for child in range(2, N+1):
    tree[child]
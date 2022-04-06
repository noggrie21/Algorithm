def dfs(v):
    visited = [0]*(N+1)
    stack = [v]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for node in sorted(g[v], reverse=True):
                if not visited[node]:
                    stack.append(node)


def bfs(v):
    q = [v]
    visited = [0] * (N+1)
    visited[v] = 1

    while q:
        v = q.pop(0)
        print(v, end=' ')
        for node in sorted(g[v]):
            if not visited[node]:
                q.append(node)
                visited[node] = visited[v] + 1


N, M, V = map(int, input().split())
g = [[] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dfs(V)
print()
bfs(V)
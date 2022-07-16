def BFS(v):
    q = [0] * N
    tree = [0] * (N+1)
    front = -1
    rear = 0
    q[rear] = v
    tree[v] = -1

    while rear != front:
        front += 1
        parent = q[front]

        for node in graph[parent]:
            if not tree[node]:
                tree[node] = parent
                rear += 1
                q[rear] = node

    return tree


N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

tree = BFS(1)

for child in tree[2:]:
    print(child)

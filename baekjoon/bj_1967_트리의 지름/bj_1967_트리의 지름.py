def DFS(node):
    visited = [-1] * (N + 1)
    visited[node] = 0
    stack = [node]

    far_node_diff = [0, 0]

    while stack:
        v = stack.pop()

        for nv, nw in weights[v]:

            if visited[nv] < 0:
                stack.append(nv)
                visited[nv] = visited[v] + nw

                if far_node_diff[1] < visited[nv]:
                    far_node_diff = [nv, visited[nv]]

    return far_node_diff


N = int(input())
weights = [[] for _ in range(N+1)]

for _ in range(N-1):
    parent, child, weight = map(int, input().split())
    weights[parent].append([child, weight])
    weights[child].append([parent, weight])

start, diff = DFS(1)
end, diff = DFS(start)
print(diff)

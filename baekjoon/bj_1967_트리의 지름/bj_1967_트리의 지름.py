def DFS(node):
    visited = [-1] * (N + 1)
    visited[node] = 0
    stack = [node]
    far_node_diff = [0, 0]

    while stack:
        v = stack.pop()
        # print(stack)

        for i in range(1, N+1):
            if weights[v][i] and visited[i] < 0:
                # print("v", "i", v, i)
                stack.append(i)
                visited[i] = visited[v] + weights[v][i]

                if far_node_diff[1] < visited[i]:
                    far_node_diff = [i, visited[i]]

    # print(visited, v, visited[v])
    print()
    return far_node_diff


N = int(input())

weights = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    parent, child, weight = map(int, input().split())
    weights[parent][child] = weights[child][parent] = weight

# print(weights)
start, diff = DFS(1)
end, diff = DFS(start)
print(diff)

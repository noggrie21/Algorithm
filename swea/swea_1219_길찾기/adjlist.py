import sys
sys.stdin = open('input (1).txt')


def dfs(v):
    global visited
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            stack += G[v]
    return visited[99]
    #         for j in G[v]:
    #             if not visited[j]:
    #                 stack.append(j)
    # if visited[99]: return 1
    # else: return 0


for _ in range(10):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))
    print(temp)
    G = [[] for _ in range(100)]
    visited = [0] * 100
    for i in range(E):
        G[temp[i*2]].append(temp[i*2+1])
        # print(i, temp[i*2], temp[i*2+1])
    # print(G)
    print(f'#{tc} {dfs(0)}')



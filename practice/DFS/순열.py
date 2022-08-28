def DFS(r, n, N):
    if r >= n:
        print(result)
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            result[r] = num[i]
            DFS(r+1, n, N)
            used[i] = 0
            result[r] = 0


N, n = map(int, input().split())

num = list(range(1, N+1))
used = [0] * N
result = [0] * n

DFS(0, n, N)


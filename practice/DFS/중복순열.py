def DFS(r, n, N):
    if r >= n:
        print(result)
        return

    for i in range(N):
        result[r] = num[i]
        DFS(r+1, n, N)
        result[r] = 0


N, n = map(int, input().split())

num = list(range(1, N+1))
used = [0] * N
result = [0] * n

DFS(0, n, N)


def DFS(r, start, n):

    if r >= n:
        print(result)
        return

    for i in range(start, N):
        if not used[i]:
            used[i] = 1
            result[r] = num[i]
            DFS(r+1, i, n)
            result[r] = 0
            used[i] = 0


N = int(input())
n = int(input())

num = list(range(1, N+1))
used = [0] * N
result = [0] * n

DFS(0, 0, n)

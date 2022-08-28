def DFS(n, N, lst):
    if n >= N:
        if lst:
            print(lst)
        return

    DFS(n+1, N, lst+[num[n]])
    DFS(n+1, N, lst)


N = int(input())
num = list(range(1, N+1))

DFS(0, N, [])
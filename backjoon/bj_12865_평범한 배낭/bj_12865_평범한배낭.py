def DFS(n, kg, v, lst):
    print(f'n:{n} kg:{kg} v:{v} lst:{lst}')
    global maxV
    global cnt
    cnt += 1
    if n >= N:
        if kg <= K and maxV < v:
            maxV = v
        return
    elif kg > K:
        return

    DFS(n+1, kg+item[n][0], v+item[n][1], lst+[item[n][0]])
    DFS(n+1, kg, v, lst)


N, K = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
cnt = 0
DFS(0, 0, 0, [])
print(maxV)
print(cnt)

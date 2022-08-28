def DFS(n, N, lst):
    global half

    if n >= N:
        total = sum(lst)
        if half == total:
            print(lst)
            return True
        return

    if DFS(n+1, N, lst+[num[n]]):
        return True
    if DFS(n+1, N, lst):
        return True


N = int(input())
num = list(map(int, input().split()))

half = sum(num) // 2
answer = 'NO'

if DFS(0, N, []):
    answer = 'YES'

print(answer)
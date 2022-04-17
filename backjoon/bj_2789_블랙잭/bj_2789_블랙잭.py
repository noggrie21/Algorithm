def nCr(r, n, start, total):
    global ans
    if total > M:
        return

    if not r:
        if ans < total:
            ans = total
        return

    for i in range(start, n):
        if not used[i]:
            used[i] = 1
            nCr(r-1, n, i+1, total + cards[i])
            used[i] = 0



# N = 카드의 개수 / M = 목표 숫자(카드 3장의 합은 M을 넘지 않고 가장 가깝게)
N, M = map(int, input().split())
cards = sorted(list(map(int, input().split())), reverse=True)
ans = 0
used = [0] * N
nCr(3, N, 0, 0)
print(ans)

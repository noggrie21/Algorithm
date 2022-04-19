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
cards =list(map(int, input().split()))
ans = 0

N, M = map(int, input().split())
cards =list(map(int, input().split()))
ans = 0

for i in range(0, N-2):
    total = 0
    total += cards[i]
    if total <= M:
        for j in range(i+1, N-1):
            total += cards[j]
            if total <= M:
                for k in range(j + 1, N):
                    total += cards[k]
                    if ans < total <= M:
                        ans = total

            else:
                total -= cards[j]

print(ans)

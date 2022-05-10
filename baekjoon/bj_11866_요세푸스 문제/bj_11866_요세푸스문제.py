N, K = map(int, input().split())
people = list(range(1, N+1))
removed = [1] * N
ans = [0] * N
n = idx = cnt = 0

while n < N:
    if removed[idx]:
        cnt += 1
    if cnt == K:
        ans[n] = f'{people[idx]}'
        removed[idx] = 0
        cnt = 0
        n += 1
    idx = (idx+1) % N

print(f'<{", ".join(ans)}>')
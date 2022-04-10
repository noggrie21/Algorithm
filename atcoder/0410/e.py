N, X, Y = map(int, input().split())
A = [0] + list(map(int, input().split()))
cnt = 0
# print(A)
for L in range(1, N+1):
    for R in range(L, N+1):
        if max(A[L:R+1]) == X and min(A[L:R+1]) == Y:
            cnt += 1
print(cnt)
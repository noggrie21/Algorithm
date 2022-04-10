N = int(input())

S = [1]

if N == 1:
    print(*S)
else:
    for n in range(2, N+1):
        S = S + [n] + S
    print(*S)

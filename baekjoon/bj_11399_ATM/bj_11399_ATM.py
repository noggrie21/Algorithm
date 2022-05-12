from sys import stdin

N = int(input())
ans = 0
lst = sorted(list(map(int, stdin.readline().rstrip().split())))

for i in range(N):
    ans += (lst[i] * (N-i))

print(ans)

import sys
sys.stdin = open('input.txt')

N = int(input())
students = [list(map(int, input().split())) for i in range(N)]
kg, cm = zip(*students)
ans = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if i != j and (kg[i] < kg[j] and cm[i] < cm[j]):
            cnt += 1
    ans[i] = cnt + 1
print(*ans)

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
ans = [0] * M
common = set(n).intersection(set(m))

card_dict = {}
for num in n:
    if num not in card_dict:
        card_dict[num] = 1
    else:
        card_dict[num] += 1

for i in range(M):
    if m[i] in common:
        ans[i] = card_dict[m[i]]

print(*ans)
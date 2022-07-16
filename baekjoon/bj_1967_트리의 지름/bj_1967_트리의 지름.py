N = int(input())
children = [[] for _ in range(13)]

for _ in range(N-1):
    p, c, weight = map(int, input().split())
    children[p].append(c)

print(N, children)
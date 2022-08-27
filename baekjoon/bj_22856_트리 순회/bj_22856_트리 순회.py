import sys
sys.setrecursionlimit(100000)


def fake_in_order(v):
    global cnt

    if v < 0:
        return -1

    visited[v] = 1
    cnt += 1

    if 0 not in visited:
        return

    left = fake_in_order(childern[v][0])
    right = fake_in_order(childern[v][1])

    if left == -1 and right == -1:
        cnt += 1


N = int(input())

cnt = 0
visited = [1] + [0] * N

history = []

# 인덱스 : 자식번호 // 값 : 부모번호
p = [0] * (N+1)

# 인덱스 : 부모번호 // 값 : 자식 번호
childern = [[] for _ in range(N+1)]

# print(tree, p, childern)

for _ in range(N):
    node, left, right = map(int, input().split())

    childern[node] = [left, right]

    if 0 < left:
        p[left] = node

    if 0 < right:
        p[right] = node

if 1 < N:
    fake_in_order(1)

print(cnt)

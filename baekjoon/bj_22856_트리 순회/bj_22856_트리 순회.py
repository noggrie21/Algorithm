import sys
sys.setrecursionlimit(100000)


def in_order(v):
    if 0 < v:
        in_order(childern[v][0])
        inorder.append(v)
        in_order(childern[v][1])


def fake_in_order(v):
    global cnt

    visited[v] = 1

    if 0 not in visited and v == inorder[-1]:
        return
    cnt += 1

    left, right = childern[v]

    if left + right < 0:
        return

    for child in childern[v]:
        if 0 < child and not visited[child]:
            fake_in_order(child)
        # print('중간쉬기', v)
        if 0 in visited:
            # print('뭐가 문제여', v)
            cnt += 1
    # if 0 < left and not visited[left]:
    #     fake_in_order(left)
    # print('중간 쉬기', v)
    # if 0 < right and not visited[right]:
    #     fake_in_order(right)
    # left = fake_in_order(childern[v][0])
    # right = fake_in_order(childern[v][1])

    # if left == -1 and right == -1:
    #     cnt += 1


N = int(input())

cnt = 0
visited = [1] + [0] * N

inorder = []

# 인덱스 : 자식번호 // 값 : 부모번호
p = [0] * (N+1)

# 인덱스 : 부모번호 // 값 : 자식 번호
childern = [[] for _ in range(N+1)]


for _ in range(N):
    node, left, right = map(int, input().split())

    childern[node] = [left, right]

    if 0 < left:
        p[left] = node

    if 0 < right:
        p[right] = node


in_order(1)
fake_in_order(1)
print(cnt)

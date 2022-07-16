N = int(input())  # 노드의 갯수

tree = [[] for _ in range(N + 1)]
print(tree)
for i in range(N):
    v1, v2 = map(int, input().split())
    print(v1, v2)
    tree[v1].append(v2)

print(tree)
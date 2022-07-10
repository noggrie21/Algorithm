def preorder(v):
    if v >= 0:
        print(chr(v + ord('A')), end='')
        preorder(tree[v][0])
        preorder(tree[v][1])


def inorder(v):
    if v >= 0:
        inorder(tree[v][0])
        print(chr(v + ord('A')), end='')
        inorder(tree[v][1])


def postorder(v):
    if v >= 0:
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(chr(v + ord('A')), end='')


N = int(input())

tree = [[] for _ in range(N)]

for _ in range(N):
    parent, *children = map(lambda x: ord(x) - ord('A') if x !='.' else -1, input().split())
    tree[parent].extend(children)


preorder(0)
print()
inorder(0)
print()
postorder(0)
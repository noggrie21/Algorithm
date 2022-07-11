def make_children():
    c = [[] for _ in range(N)]

    for child in range(N):
        parent = p[child]

        if parent >= 0:
            c[parent].append(child)

    return c


def delete_node(v):
    p[v] = 50
    children = c[v]

    if children:
        c[v] = []

        for child in children:
            delete_node(child)


def count_leaf():
    result = 0

    for node in range(N):
        if not c[node] and p[node] != 50:
            result += 1

    return result


N = int(input())
p = list(map(int, input().split()))
v = int(input())

if p[v] == -1:
    print(0)
else:
    c = make_children()
    c[p[v]].remove(v)
    delete_node(v)
    print(count_leaf())

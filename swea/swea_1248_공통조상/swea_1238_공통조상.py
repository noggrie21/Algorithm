import sys
sys.stdin = open('input (1).txt')


def set_relation(E):
    for i in range(E):
        p, c = array[i * 2], array[i * 2 + 1]
        parent[c] = p
        if not ch1[p]:
            ch1[p] = c
        else:
            ch2[p] = c


def search_forebear(v):
    forebear = []
    while parent[v]:
        forebear.append(parent[v])
        v = parent[v]
    return forebear


def find_common(array1, array2):
    for elem in array1:
        if elem in array2:
            return elem


def post_order(v):
    global children
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        children.append(v)


T = int(input())

for tc in range(1, T + 1):
    V, E, v1, v2 = map(int, input().split())
    array = list(map(int, input().split()))
    parent = [0] * (V + 1)                   # 자식 노드 번호를 인덱스로 하는 부모배열
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    set_relation(E)
    v1_forebears = search_forebear(v1)
    v2_forebears = search_forebear(v2)
    sub_root = find_common(v1_forebears, v2_forebears)
    children = []
    post_order(sub_root)
    print(f'#{tc} {sub_root} {len(children)}')
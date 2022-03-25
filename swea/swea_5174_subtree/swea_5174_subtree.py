import sys
sys.stdin = open('sample_input.txt')


def make_tree(E):                                       # [[0, 0], [6, 0], [1, 5], [0, 0], [0, 0], [3, 0], [4, 0]]
    child = [[0, 0] for _ in range(V + 1)]
    for i in range(E):                                  # 부모 노드 번호를 인덱스로 하는 자식 노드 저장
        if not child[array[i * 2]][0]:
            child[array[i * 2]][0] = array[i * 2 + 1]
        else:
            child[array[i * 2]][1] = array[i * 2 + 1]
    return child


def pre_order(v):                                       # 순회하면서 다른 노드로 이동할 때마다 cnt += 1
    global cnt
    if v:
        cnt += 1
        pre_order(child[v][0])                          # 왼쪽 자식 노드로 GO!
        pre_order(child[v][1])                          # 오른쪽 자식 노드로 GO!


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())                    # E: 간선의 갯수 / N: 서브트리의 루트노드
    array = list(map(int, input().split()))
    V = E + 1
    child = make_tree(E)
    cnt = 0
    pre_order(N)
    print(f'#{tc} {cnt}')


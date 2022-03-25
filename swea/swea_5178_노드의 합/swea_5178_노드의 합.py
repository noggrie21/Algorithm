import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    # N: 노드의 개수 / M: 리프노드의 개수 / L: 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    # 리프 노드를 인덱스로 하여 저장 값 넣어주기
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    # 리프 노드에서부터 하나씩 부모 노드에 값 남겨놓기
    for node in range(N, L, -1):
        tree[node//2] += tree[node]
    print(f'#{tc} {tree[L]}')

import sys
sys.stdin = open('input (1).txt')

# 완전 이진 트리
# 정점 하나당 알파벳 하나
# 루트노드 번호 : 1


def in_order(v):
    if v <= V:
        in_order(v*2)
        print(chr[v], end='')
        in_order(v*2+1)


for tc in range(1, 11):
    V = int(input())
    chr = [0] * (V + 1)
    for v in range(V):
        temp = list(input().split())
        chr[int(temp[0])] = temp[1]
    print(f'#{tc} ', end='')
    in_order(1)
    print()
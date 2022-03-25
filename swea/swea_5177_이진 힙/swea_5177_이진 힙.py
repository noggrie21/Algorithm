import sys
sys.stdin = open('sample_input.txt')

# 1. 마지막 노드 뒤에 새 노드를 추가
# 2. 부모 노드 값 > 자식 노드 값

def make_tree(values):
    last = 0                                                             # 마지막 노드의 번호를 가르킴(현재는 values에서 꺼낸 적이 없어서 0을 가르킴)
    for value in values:
        last += 1
        tree[last] = value
        temp = last                                                      # 부모 노드와의 비교를 위해 임시 변수 tmep에 last 담기
        while 1 <= temp // 2 and tree[temp // 2] > tree[temp]:           # 부모 노드가 존재할 때, 부모 노드 값 > 자식 노드 값
            tree[temp // 2], tree[temp] = tree[temp], tree[temp // 2]    # 서로 값을 바꿔주고
            temp = temp // 2                                             # 더 상위 부모와 비교하기 위해 temp를 부모 노드 번호로 재할당


def sum_parents(v):
    total = 0
    while 1 <= v:                                                        # 해당 노드가 존재하면
        v //= 2                                                          # 부모 노드로 바꿔서
        total += tree[v]                                                 # 부모 노드 값 합산
    return total


T = int(input())

for tc in range(1, T + 1):
    N = int(input())                                                    # N: 노드의 갯수
    values = list(map(int, input().split()))                            # 각 노드에 저장될 값들(서로 다른 자연수)
    tree = [0] * (N + 1)                                                # 각 노드 번호를 인덱스로하여 노드가 갖을 값 저장
    make_tree(values)                                                   # 각 노드에 저장될 값 찾기
    result = sum_parents(N)
    print(f'#{tc} {result}')


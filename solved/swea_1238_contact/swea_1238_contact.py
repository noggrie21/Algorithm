import sys
sys.stdin = open('input (1).txt')


# 비상연락망 정보 => 가장 나중에 연락받게 되는 사람 중 번호가 가장 큰 사람


def set_contact(contact, N):
    for i in range(N//2):
        contact[edges[i * 2]].append(edges[i * 2 + 1])


def bfs(v):
    queue = [v]
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        for next in contact[v]:
            if not visited[next]:
                queue.append(next)
                visited[next] = visited[v] + 1
    return visited[v]


def find_idx(value, array):
    max_idx = 0
    for i in range(101):
        if value == array[i] and max_idx < i:
            max_idx = i
    return max_idx


for tc in range(1, 11):
    N, v = map(int, input().split())
    edges = list(map(int, input().split()))
    contact = [[] for _ in range(101)]
    set_contact(contact, N)
    visited = [0] * 101
    ans = find_idx(bfs(v), visited)
    print(f'#{tc} {ans}')


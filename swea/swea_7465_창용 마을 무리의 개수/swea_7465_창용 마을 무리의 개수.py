import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())


def BFS(i):
    queue = [i]

    while queue:
        # deque하기
        i = queue.pop(0)

        # queue에 삽입하기
        for j in graph[i]:
            if not checked[j]:
                checked[j] = 1
                queue.append(j)


for tc in range(1, T+1):
    N, M = map(int, (input().split())) # N: 마을 주민 수, M: 마을 주민의 관계 수
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    checked = [0]*(N+1)
    ans = 0

    for i in range(1, N+1):
        if not checked[i]:
            checked[i] = 1
            BFS(i)
            ans += 1

    print(f'#{tc} {ans}')


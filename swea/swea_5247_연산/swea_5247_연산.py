from collections import deque


T = int(input())


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1                                       # 기본 연산 횟수를 1로 시작함(중복 결과 값인지 아닌지 구별하기 위해)

    while queue:
        v = queue.popleft()

        if not v ^ M:                                    # 만일 찾는 값(M)이 나오면
            return visited[v] - 1                        # 함수 종료(연산 횟수 반환)

        for num in [v+1, v-1, v*2, v-10]:                # v의 연산 결과를 하나씩 꺼내보면서,
            if 0 < num <= 1000000 and not visited[num]:  # 범위를 벗어나거나, 이미 나온 수라면 queue에 담지 않음
                queue.append(num)
                visited[num] = visited[v] + 1            # visited[num]에는 v에서 num이 될 때까지의 연산 횟수(+1)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print(f'#{tc} {BFS(N)}')
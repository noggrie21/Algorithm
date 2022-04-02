from collections import deque


def search_coordinate():
    virous = [] # 바이러스의 좌표가 담길 배열
    blank = [] # 빈칸의 좌표가 담길 배열 (벽을 세울 수 있는 후보를 구하기 위해)

    # 연구소를 순회하면서 virous와 blank 채우기
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                virous.append((i, j))
            elif not lab[i][j]:
                blank.append((i, j))

    return virous, blank


def nCr(s, r, start, N, selected = []): # s: 현재까지 고른 벽의 갯수, r: 골라야할 벽의 총 갯수(문제에선 3으로 고정), N: 벽이 될 수 있는 빈칸의 총 갯수, selected: 벽을 세울 위치
    global ans

    # 기저 파트(벽 세울 곳을 모두 고름)
    if s >= r:
        for i, j in selected:                                     # 벽을 세울 위치가 담긴 배열을 순회하며
            lab[i][j] = 1                                         # 벽을 세움

        result = BFS(N-3)                                         # 벽이 될 수 있는 빈칸 N개 방금 3개의 벽을 세웠으니 -3하고 BSF로 넘겨줌(N-3은 안전영역의 초기값)
        ans = max(ans, result)                                    # BFS의 반환값과 ans 중 최댓값으로 갱신

        for i, j in selected:                                     # 다음 조합을 위해 벽 부수기
            lab[i][j] = 0

        return

    # 유도 파트(벽을 세울 3곳을 고르지 못함)
    else:
        for i in range(start, N):
            if not used[i]:
                used[i] = 1
                nCr(s+1, r, i+1, N, selected + [blank[i]])
                used[i] = 0


def BFS(safe):
    global ans

    # 생성
    queue = deque()
    visited = [[0]*M for _ in range(N)]

    # 초기화
    for i, j in virous:
        visited[i][j] = 1
        queue.append((i, j))

    # BFS
    while queue:
        # 좌표 하나씩 뽑기(바이러스 또는 바이러스에 감염된 좌표)
        i, j = queue.popleft()

        # 안전영역이 구해진 최대의 안전영역보다 작은 경우 탐색 종료
        if ans > safe:
            return 0

        # 큐에 삽입되는 파트(= 바이러스가 전염될 수 있는 곳인가를 확인)
        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and not lab[ni][nj]:     # 상하좌우가 방문한 적이 없고(=not visited[ni][nj]), 빈칸인 경우(=not lab[ni][nj])
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))
                safe -= 1                                                                   # 바이러스가 해당 칸으로 이동할 수 있다 == 안전영역이 하나 줄어든다.

    return safe


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virous, blank = search_coordinate()
n = len(blank)
used = [0] * n
ans = 0
nCr(0, 3, 0, n)
print(ans)

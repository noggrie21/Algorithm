from collections import deque
'''
1: 익은 토마토
0: 익지 않은 토마토
-1: 토마토 없음
출력: 토마토가 모두 익을 때까지의 최소 날짜
(처음부터 모두 익어있으면 0, 모두 익지 못하면 -1)

1. 1인 좌표 리스트 구하기(반복문)
(한번도 0을 만나지 못하면 0 리턴)
2. q에 1리스트 넣고 bfs돌리기
3. q에 넣는 조건 not visited일때, 
'''


def check(N, M):
    # 변수와 배열 생성 및 초기화
    unripe = 0                              # unripe: 익지 않은 토마토 개수
    queue = deque()                         # 익지 않은 토마토가 존재하면 BFS탐색에 쓰일 queue
    visited = [[0] * M for _ in range(N)]   # 마찬가지로 BFS탐색이 진행되면 쓰일 visited 배열

    # 토마토 상태 확인하기
    for r in range(N):
        for c in range(M):
            if not totato[r][c]:            # 익지 않은 토마토면,
                unripe += 1                 # unripe += 1
            elif totato[r][c] == 1:         # 익은 토마토면,
                queue.append((r, c))        # BFS에 쓰일 queue에 삽입
                visited[r][c] = 1           # vistied 표시

    # 토마토 상태에 따라 처리하기
    if not unripe:                          # 익지 않은 토마토가 없으면
        return 0                            # 0 리턴
    return BFS(queue, visited, unripe)      # 익지 않은 토마토가 있으면 익은 토마토를 시작점들로 하는 BFS 탐색하기


def BFS(queue, visited, unripe):
    ripe = 0                                # ripe: 익힌 토마토(익지 않은 -> 익은) 개수

    while queue:
        r, c = queue.popleft()

        for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not totato[nr][nc]:  # 익은 토마토 주변에 익지 않은 토마토가 존재하면
                visited[nr][nc] = visited[r][c] + 1                                         # 소요시간 기록하기
                queue.append((nr, nc))                                                      # 익은 토마토를 나타내는 queue에 삽입하기
                ripe += 1                                                                   # 익은 토마토 + 1

    if ripe == unripe:                                                                      # 익지 않은 토마토와 익힌 토마토 개수가 동일
        return visited[r][c] - 1                                                            # 마지막으로 익은 토마토의 위치를 나타내는 (r,c)의 (visited 값 - 1)
    else:                                                                                   # 익지 않은 토마토가 남았다면,
        return -1                                                                           # -1 반환


M, N = map(int, input().split())                                                            # M: 가로 크기 N: 세로 크기 (2<=M, N<=1,000)
totato = [list(map(int, input().split())) for _ in range(N)]
print(check(N, M))
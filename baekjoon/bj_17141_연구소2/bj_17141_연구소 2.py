from copy import deepcopy
from collections import deque
from itertools import combinations


def search_point(area, point):
    '''
    :param area: 탐색 대상이 되는 2차원 배열
    :param point: 탐색 기준이 되는 점수
    :return: 탐색 결과(탐색 기준에 부합하는 좌표 배열)
    '''
    points = []

    for r in range(N):
        for c in range(N):
            if area[r][c] == point:
                points.append((r, c))

    return points


def BFS(selected):
    '''
    :param selected: r개의 바이러스 놓을 좌표 배열
    :return: 바이러스가 퍼지는 시간, 바이러스가 퍼진 실험실 상태
    '''
    q = deque()
    q.extend(selected)

    copy_lab = deepcopy(lab)

    for r, c in points:
        if (r, c) in selected:
            copy_lab[r][c] = 1
        else:
            copy_lab[r][c] = 0

    while q:
        cr, cc = q.popleft()

        for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and not copy_lab[nr][nc]:
                copy_lab[nr][nc] = copy_lab[cr][cc] + 1
                q.append((nr, nc))

    return copy_lab[cr][cc]-1, copy_lab


def nCr(n, r):
    '''
    :param n: 바이러스 배치 가능한 좌표 배열
    :param r: 바이러스 배치 갯수
    '''
    global answer

    for selected in combinations(n, r):
        times, copy_lab = BFS(selected)

        if not search_point(copy_lab, 0):
            answer = min(answer, times)


N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]
answer = 2500

points = search_point(lab, 2)

nCr(points, M)

if answer == 2500:
    print(-1)
else:
    print(answer)



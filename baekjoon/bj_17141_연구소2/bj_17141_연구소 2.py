from copy import deepcopy
from collections import deque
from itertools import combinations


def search_point(area, point):
    '''
    :param area: 연구소 같은 탐색 대상이 되는 2차원 배열
    :param point: 탐색 기준이 되는 점수
    :return: 탐색 결과(갯수, 탐색 기준에 부합하는 좌표 배열)
    '''
    n = 0
    points = []

    for r in range(N):
        for c in range(N):
            if area[r][c] == point:
                n += 1
                points.append((r, c))

    return n, points


def BFS(selected):
    '''
    :param selected: 바이러스 놓을 좌표 배열
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


def nCr(r, start, last, selected):
    '''
    :param r: 바이러스 개수
    :param start: 조합의 범위 시작점
    :param last: 조합의 범위 끝점
    :param selected: 선택된 조합이 담긴 배열
    '''
    global answer

    # 기저 파트
    if not r:
        times, copy_lab = BFS(selected)

        if not search_point(copy_lab, 0)[0]:
           answer = min(answer, times)

        return

    # 유도 파트
    else:
        for i in range(start, last):
            nCr(r-1, i+1, last, selected + [points[i]])

        return


N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]
answer = 2500

n, points = search_point(lab, 2)

nCr(M, 0, n, [])

if answer == 2500:
    print(-1)
else:
    print(answer)



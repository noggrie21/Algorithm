'''
선생님(T), 학생(S), 장애물(O), 빈칸
선생님 감시 가능 : 상, 하, 좌, 우(단, 장애물 뒤에는 볼 수 없음)
'''

# print(ord('S'), ord('T'), ord('O'), ord('X'))


def switch(char):
    if char == 'S':  # 학생
        return 2
    elif char == 'T':  # 선생
        return 3
    elif char == 'X':  # 빈칸
        return 0
    return 1  #  장애물


def asign(school, N):
    empty, teacher = [], []

    for r in range(N):
        for c in range(N):
            if school[r][c] == 3:
                teacher.append([r, c])
            if not school[r][c]:
                empty.append([r, c])

    return empty, teacher


def toggle(candidate, status):
    for r, c in candidate:
        school[r][c] = status


def is_possible(candidate):
    toggle(candidate, 1)

    for r, c, in teacher:
        for dr, dc in (0, 1), (1, 0), (-1, 0), (0, -1):
            for k in range(1, N):
                nr, nc = r + dr * k, c + dc * k
                if 0 <= nr < N and 0 <= nc < N:
                    if school[nr][nc] == 2:
                        toggle(candidate, 0)
                        return False
                    elif school[nr][nc] == 1:
                        break
    return True


def nCr(r, N, start, candidate):
    global answer

    # 가지치기
    if answer == 'YES':
        return

    # 종료 파트
    if r <= 0:
        # print(candidate)
        if is_possible(candidate):
            answer = 'YES'
        return

    for i in range(start, N):
        if not used[i]:
            used[i] = 1
            nCr(r-1, N, i, candidate + [empty[i]])
            used[i] = 0


N = int(input())
empty = []
school = [list(map(lambda x: switch(x), input().split())) for _ in range(N)]

empty, teacher = asign(school, N)
E = len(empty)
used = [0] * E
answer = 'NO'

nCr(3, E, 0, [])

print(answer)
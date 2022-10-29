import sys
sys.stdin = open('sample_input.txt')

T = int(input())
delta = [[],[1, 0], [0, 1], [-1, 0], [0, -1]]


def search_maxinos(N):
    maxinos = []
    connected_core = 0

    for r in range(N):
        for c in range(N):
            if proccesor[r][c]:
                if r in [0, N-1] or c in [0, N-1]:
                    connected_core += 1
                else:
                    maxinos.append([r, c])

    print(f'core:{connected_core} / maxnios:{maxinos}')
    return connected_core, maxinos


def nCn(r, n, cnt, diffs):
    global answer
    global temp

    print(r, n, cnt, diffs)
    print(f'used:{used}')
    # 가지치기
    if answer[1] < diffs:
        return 0

    # 종료파트
    if n <= r:
        if answer[0] < cnt or answer[0] == cnt and diffs <= answer[1]:
            answer[0] = cnt
            answer[1] = diffs
        return

    for k in range(1, 5):
        used[r] = k
        possibility, diff = connect(maxinos[r][0], maxinos[r][1], delta[k]), temp
        print(f'??used:{used} possibility{possibility} diff{diff}')
        nCn(r+1, n, cnt+possibility, diffs+diff)
        used[r] = 0


def connect(r, c, direction):
    global N
    global temp

    if not 0 <= r < N and not 0 <= c < N:
        return 1

    if proccesor[r][c]:
        temp = 0
        return 0

    nr = r + direction[0]
    nc = c + direction[1]

    if connect(nr, nc, direction):
        proccesor[r][c] = 1
        temp += 1
        return 1


for tc in range(1, T+1):
    N = int(input())

    proccesor = [list(map(int, input().split())) for _ in range(N)]
    answer = [0, 12*12]

    maxinos = []
    answer[0], maxinos = search_maxinos(N)
    print(f'maxinos: {maxinos}')

    n = len(maxinos)
    used = [0] * n
    temp = 0

    nCn(0, n, answer[0], 0)

    print(f'#{tc} {answer[1]}')

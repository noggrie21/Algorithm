from copy import deepcopy
import sys
sys.stdin = open('sample_input.txt')


def BFS(N):
    global tc
    cnt = 0
    q = [[cnt, N, deepcopy(cards)]]
    half = N//2

    while cnt < 6:
        # print('q:', q)
        cnt, N, now_cards = q.pop(0)

        L, R = now_cards[:half], now_cards[half:]

        if tc == 4:
            print('cnt:', cnt, 'N:', N, 'now_cards:', now_cards)
            print('L', L, 'R', R)

        for x in range(1, N):
            new_cards = deepcopy(suffle(L, R, x, half))

            if tc == 4:
                print('new_cards:', new_cards, 'x', x, 'cnt',cnt)

            if isSorted(new_cards):
                return cnt + 1

            q.append([cnt+1, N, new_cards])
            # print('q',q)

    return -1


def suffle(L, R, x, half):
    L, R, x = switch(L, R, x, half)
    step = half - x
    result = []

    if not x:
        result = L + R
        return result

    left_start = right_start = 0
    while left_start < half:
        result += L[left_start:left_start+step] + [R[right_start]]
        left_start += step
        right_start += 1

    result += R[right_start:]

    return result


def isSorted(lst):
    if lst == ascending or lst == descending:
        return True
    return False


def switch(L, R, x, half):
    if half <= x:
        L, R = R, L
        x = (N - 1) - x
    return L, R, x


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    cards = list(map(int, input().split()))
    answer = 0

    ascending = sorted(cards)
    descending = sorted(cards, reverse=True)

    if not isSorted(cards):
        print('cards', cards)
        answer = BFS(N)

    print(f'#{tc} {answer}')

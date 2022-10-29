from itertools import product
from pprint import pprint
from copy import deepcopy
import sys
sys.stdin = open('sample_input (1).txt')


def throw_bomb(c):
    cnt = 1
    bomb = [[temp_top[c], c, temp_matrix[temp_top[c]][c]]]
    temp_top[c] += 1

    while bomb:
        r, c, diff = bomb.pop(0)
        temp_matrix[r][c] = 0

        if tc == 2:
            pprint(temp_matrix)
            print(r, c, diff)

        for dr, dc in (0, 1), (1, 0), (-1, 0), (0, -1):
            # print(matrix[r][c])
            for k in range(diff):
                nr = r + (dr * k)
                nc = c + (dc * k)

                if 0 <= nr < H and 0 <= nc < W and 1 <= temp_matrix[nr][nc]:
                    if tc == 2:
                        print(k, nr, nc, temp_matrix[nr][nc])


                    if 1 < temp_matrix[nr][nc]:
                        bomb.append([nr, nc, temp_matrix[nr][nc]])
                        if tc == 2:
                            print('bomb', bomb)
                        # temp_matrix[nr][nc] = 0

                    if temp_top[nc] < nr:
                        for br in range(nr, temp_top[nc], -1):
                            temp_matrix[br][nc] = temp_matrix[br-1][nc]
                            temp_matrix[temp_top[nc]][nc] = 0

                    cnt += 1
                    temp_matrix[nr][nc] = 0
        if tc == 2:
            print(bomb)
    if tc == 2:
            # pprint(temp_matrix)
        print('끝', cnt, temp_top)
    return cnt


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]

    # top 구하기
    top = [H-1] * W
    for c in range(W):
        for r in range(H):
            if matrix[r][c]:
                top[c] = r
                break
    # print(top)


    # 중복순열 구하기
    set_bomb = list(product(range(W), repeat=N))
    # print(set_col)

    # 하나씩 경우의 수 따져보기
    answer = 0

    for case in set_bomb:
        cnt = 0
        temp_top = deepcopy(top)
        temp_matrix = deepcopy(matrix)
        if tc == 2:
            print(case)
        for col in case:

            if temp_top[col] >= H:
                continue
            cnt += throw_bomb(col)
        if answer < cnt:
            answer = cnt
        if tc == 2:
            print('다음 case', answer, cnt)

    print(f'#{tc} {answer}')

arr = [[4, 5, 7, 1, 6, 3, 8, 2, 9], [6, 3, 9, 8, 2, 7, 5, 4, 1], [7, 9, 3, 4, 8, 5, 1, 6, 2], [1, 8, 2, 5, 4, 9, 6, 3, 7], [8, 6, 1, 7, 9, 2, 3, 5, 4], [5, 2, 4, 6, 3, 1, 7, 9, 8], [3, 7, 6, 9, 1, 4, 2, 8, 5], [2, 4, 5, 3, 7, 8, 9, 1, 6], [9, 1, 8, 2, 5, 6, 4, 7, 3]]

result = 1
di = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1, 0]

# 행 확인
for i in range(9):
    total = 0
    counts_r = [0] * 10
    for j in range(9):
        counts_r[arr[i][j]] = 1
    for count in counts_r:
        total += count
    if total == 9:
        result *= 1
    else:
        result *= 0

# 열 확인
for i in range(9):
    total = 0
    counts_c = [0] * 10
    for j in range(9):
        counts_c[arr[j][i]] = 1
    for count in counts_c:
        total += count
    if total == 9:
        result *= 1
    else:
        result *= 0

# 사각형 확인
for i in range(1, 9, 3):
    total = 0
    counts_b = [0] * 10
    for j in range(1, 9, 3):
        for k in range(9):
            ni = di[k] + i
            nj = dj[k] + j
            counts_b[arr[ni][nj]] = 1
    for count in counts_b:
        total += count
    if total == 9:
        result *= 1
    else:
        result *= 0

print(result)

    # if (i % 3) * (j % 3) == 1:
    #     for k in range(9):
    #         ni = di[k] + i
    #         nj = dj[k] + j
    #         if 0 <= ni < 9 and 0 <= nj < 9:
    #             counts_b[arr[ni][nj]] = 1
    #
    # for idx in range(9):
    #     if not counts_r[idx]*counts_c[idx]*counts_b[idx]:
    #         print(f'{tc} 0')
    #         break
    # else:
    #     print(f'{tc} 1')
    #
    #
    # for count in counts:
    #     total += count
    # if total == 9:
    #     result *= 1
    # else:
    #     result *= 0
    #
    # # 열 확인
    # counts = [0] * 10
    # for i in range(9):
    #     for j in range(9):
    #         counts[arr[j][i]] = 1
    # for count in counts:
    #     total += count
    # if total == 9:
    #     result *= 1
    # else:
    #     result *= 0
    #
    # # 사각형 확인
    # counts = [0] * 10
    #

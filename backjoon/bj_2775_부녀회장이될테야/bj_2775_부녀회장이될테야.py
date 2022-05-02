apart = [list(range(15))] + [[0, 1] + [0] * 13 for _ in range(14)]

for r in range(1, 15):
    for c in range(2, 15):
        apart[r][c] = apart[r][c-1] + apart[r-1][c]

N = int(input())
for _ in range(N):
    floor = int(input())
    number = int(input())
    print(apart[floor][number])

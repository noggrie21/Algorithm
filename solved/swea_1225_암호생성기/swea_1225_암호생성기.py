import sys
sys.stdin = open('input (1).txt')

for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    result = [0] * 8
    i = 0
    switch = True
    while switch:
        for step in range(1, 6):
            if arr[i] - step <= 0:
                arr[i] = 0
                switch = False
                break
            arr[i] = arr[i] - step
            i = (i + 1) % 8
    for j in range(8):
        result[j] = arr[(j + i + 1) % 8]
    print(f'#{tc}', *result)


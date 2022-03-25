import sys
sys.stdin = open('input (1).txt')

def binary(candidates, key):
    n = len(candidates)
    minK = key
    for i in range(1, 2**n):
        total = 0
        for j in range(n):
            if i & (1 << j):
                total += candidates[j]
        new = key - total
        if new >= 0 and new < minK:
            minK = new
    return minK

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split()) # N: 점원의 수 / B: 탑의 높이
    heights = list(map(int, input().split())) # heights: 점원의 키 정보 / S = sum(heights)
    selection_sort(N)
    total = sum_heights(heights)
    key = total - B
    candidates = list(filter(le, heights))
    ans = compare(key, candidates)
    print(f'#{tc}', ans)

import sys
sys.stdin = open('input (1).txt')

# 출력 : 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑 찾기(B 이상인 수에서 가장 작은 차이)
# 1 <= N(점원의 수) <= 20
# 1 <= B(탑의 높이) <= 점원 키 총 합계


def le(number):
    global key
    if key - number >= 0:
        return True
    return False


def compare(key, candidates):
    if not candidates:
        return key
    elif key == candidates[-1]:
        return 0
    else:
        key = binary(candidates, key)
        return key


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
    N, B = map(int, input().split())          # N: 점원의 수 / B: 탑의 높이
    heights = list(map(int, input().split())) # heights: 점원의 키 정보
    heights.sort()
    total = sum(heights)
    key = total - B                           # key : 점원들 키 - 탑의 높이
    candidates = list(filter(le, heights))    # candidates : key보다 작은 점원만 담겨있는 배열
    print(candidates)
    ans = compare(key, candidates)
    print(f'#{tc}', ans)



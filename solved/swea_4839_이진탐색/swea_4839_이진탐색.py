import sys
sys.stdin = open('sample_input.txt')


def binary_s(k, P):  # k: 찾는 페이지 P: 전체 페이지
    left = 1
    right = P
    cnt = 0
    while left <= right:
        c = int((left + right) / 2)
        cnt += 1
        if c == k:
            return cnt
        elif c > k:
            right = c
        else:
            left = c


T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    a = binary_s(Pa, P)
    b = binary_s(Pb, P)
    if a > b:
        print(f'#{tc} B')
    elif a < b:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')

import sys
sys.stdin = open('sample_input.txt')


binary = [0] * 40
ternary = [0] * 40
for i in range(40):
    binary[i] = 2 ** i
    ternary[i] = 3 ** i


def pick_out(N):
    candidates = []
    for i in range(N):
        num1[i] = num1[i] ^ 1
        total = 0
        for j in range(N):
            total += num1[j] * binary[N - 1 - j]
        candidates.append(total)
        num1[i] = num1[i] ^ 1
    return candidates


def search(M):
    for i in range(M):
        cnt = 0
        while cnt != 2:
            num2[i] = (num2[i]+1) % 3
            total = 0
            for j in range(M):
                total += num2[j] * ternary[M-1-j]
            if total in candidates:
                return total
            cnt += 1
        num2[i] = (num2[i] + 1) % 3


T = int(input())

for tc in range(1, T + 1):
    num1 = list(map(int, input()))
    num2 = list(map(int, input()))
    N, M = len(num1), len(num2)
    candidates = pick_out(N)
    ans = search(M)
    print(f'#{tc} {ans}')
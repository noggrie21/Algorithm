import sys
sys.stdin = open('sample_input.txt')


binary = [0] * 40  # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...]
ternary = [0] * 40  # [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, ...]
for i in range(40):
    binary[i] = 2 ** i
    ternary[i] = 3 ** i


def pick_out(num, N, base, lookup):
    candidates = set()  # 한 자리씩 변경 후 10진수로 변환하여 담을 예정

    for i in range(N):
        temp = num[i]   # num[i]의 초기값을 temp에 보관
        while True:
            num[i] = (num[i] + 1) % base # num[i]값 바꿔보기 (+1하되 base를 넘지 않도록 조정)
            if num[i] == temp:   # num[i]의 초기값인 temp와 같아지면 while 종료
                break
            total = 0
            for j in range(N):   # num[i]값이 변경된 상태에서 10진수 값 구하기
                total += num[j] * lookup[N - 1 - j]
            candidates.add(total)
    return candidates


T = int(input())


for tc in range(1, T + 1):
    num1 = list(map(int, input()))   # num1과 num2는 값을 하나씩 변경해볼 거라 리스트로 받음
    num2 = list(map(int, input()))
    set1 = pick_out(num1, len(num1), 2, binary)
    set2 = pick_out(num2, len(num2), 3, ternary)
    ans = set1.intersection(set2)
    print(f'#{tc}', *ans)

    
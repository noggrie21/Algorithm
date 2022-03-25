import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for tc in range(1, T+1):
    x = input().split()
    N = int(x[1])
    num = input().split()
    num_key = set(num)
    num_dict = {}

    # 숫자 체계를 키로 한 딕셔너리
    for key in num_key:
        num_dict[key] = 0

    for i in range(N):
        num_dict[num[i]] += 1

    result = []

    print(num_dict)
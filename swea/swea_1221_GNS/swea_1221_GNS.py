import sys
sys.stdin = open('GNS_test_input.txt')

num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())

for tc in range(1, T+1):
    x = input().split()
    N = int(x[1])
    num = input().split()

    counts = [0] * 10

    # 카운트 배열 만들기
    for i in range(N):
        num[i]
    # print(counts)

    # 누적 카운트 배열 만들기
    # temp = [counts[0]] + [0] * 9
    # for i in range(1, 10):
    #     temp[i] = temp[i-1] + counts[i]
    # print(temp)

    # ㄱ
    result =[]
    for i in range(10):
        if i == 0:
            while counts[i]:
                result += ['ZRO']
                counts[i] -= 1
        elif i == 1:
            while counts[i]:
                result += ['ONE']
                counts[i] -= 1
        elif i == 2:
            while counts[i]:
                result += ['TWO']
                counts[i] -= 1
        elif i == 3:
            while counts[i]:
                result += ['FOR']
                counts[i] -= 1
        elif i == 4:
            while counts[i]:
                result += ['ZRO']
                counts[i] -= 1
        elif i == 5:
            while counts[i]:
                result += ['FIV']
                counts[i] -= 1
        elif i == 6:
            while counts[i]:
                result += ['SIX']
                counts[i] -= 1
        elif i == 7:
            while counts[i]:
                result += ['SVN']
                counts[i] -= 1
        elif i == 8:
            while counts[i]:
                result += ['EGT']
                counts[i] -= 1
        else:
            while counts[i]:
                result += ['NIN']
                counts[i] -= 1
    print(f'#{tc}')
    print(*result)
        # elif num[i] == 'ONE': counts[1] += 1
        # elif num[i] == 'TWO': counts[2] += 1
        # elif num[i] == 'THR': counts[3] += 1
        # elif num[i] == 'FOR': counts[4] += 1
        # elif num[i] == 'FIV': counts[5] += 1
        # elif num[i] == 'SIX': counts[6] += 1
        # elif num[i] == 'SVN': counts[7] += 1
        # elif num[i] == 'EGT': counts[8] += 1
        # else: counts[9] += 1


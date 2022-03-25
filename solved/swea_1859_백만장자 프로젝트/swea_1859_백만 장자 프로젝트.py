import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(3):
    N = int(input())
    price = list(map(int, input().split())) + [0]
    total = 0
    temp = []

    for i in range(N):
        if price[i] <= price[i+1]:
            temp.append(price[i])
        else:
            if temp:
                for j in temp:
                    total += price[i] - j
                    temp = []
    print(f'#{tc} {total}')






import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    # print(f'{N} {M} {array}')

    for n in range(M):
        array.append(array.pop(0))
        # print(array)
    print(f'#{tc} {array[0]}')

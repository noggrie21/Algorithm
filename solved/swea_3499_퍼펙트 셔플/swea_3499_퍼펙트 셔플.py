import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    a = N//2
    result = []
    for i in range(a):
        result.append(arr[-1-N:-a][i])
        result.append(arr[-a:][i])
    if N % 2:
        result.append(arr[-1-N:-a][-1])
    print(f'#{tc}', *result)
import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def recur(num, end, cnt, lst):
    global ans
    print(lst, cnt)
    if ans < cnt:
        return

    if num >= end:
        cnt -= 1
        ans = min(ans, cnt)

    else:
        for i in range(arr[num], 0, -1):
            recur(num+i, end, cnt+1, lst+[num+i])


for tc in range(1, T+1):
    N, *arr = map(int, input().split())
    arr = [0] + arr + [0]
    ans = N
    recur(1, N, 0, [1])
    print(f'#{tc} {ans}')
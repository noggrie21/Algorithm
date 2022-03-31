import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())


def merge_sort(lst):
    global cnt

    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    if left[-1] > right[-1]:
        cnt += 1

    l = r = k = 0
    L = len(left)
    R = len(right)

    while l < L and r < R:
        if left[l] > right[r]:
            lst[k] = right[r]
            r += 1
        else:
            lst[k] = left[l]
            l += 1
        k += 1

    if l < L:
        lst[k:] = left[l:]
    else:
        lst[k:] = right[r:]

    return lst


for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    lst = merge_sort(lst)
    print(f'#{tc} {lst[N//2]} {cnt}')
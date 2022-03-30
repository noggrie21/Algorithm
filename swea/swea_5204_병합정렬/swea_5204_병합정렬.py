import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def merge_sort(arr):
    global cnt

    # 기본 파트
    if len(arr) == 1:
        return arr

    # 유도 파트
    else:
        mid = len(arr) // 2     # arr 반으로 가르기
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        if left[-1] > right[-1]:
            cnt += 1

        return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    L = len(left)
    R = len(right)

    while i < L or j < R:
        if i < L and j < R:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < L:
            result.extend(left[i:])
            break
        else:
            result.extend(right[j:])
            break

    return result


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{tc} {result[N//2]} {cnt}')



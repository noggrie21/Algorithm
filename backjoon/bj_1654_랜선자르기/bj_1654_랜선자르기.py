def binary_search(end):
    start = 1
    maxlength = 0

    while start <= end:
        middle = (start + end) // 2
        print('line7', start, middle, end)
        cnt = 0

        for cable in lst:
            print(cable, middle, cable // middle)
            cnt += cable // middle
        print(cnt)

        if cnt == N:
            maxlength = max(maxlength, middle)
            start = middle + 1

        elif cnt > N:
            start = middle + 1

        else:
            end = middle - 1

    return maxlength


K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
if K == N:
    print(min(lst))
# print(lst)
print(binary_search(min(lst)))
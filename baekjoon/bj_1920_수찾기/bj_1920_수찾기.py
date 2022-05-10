def binarysearch(number, end): # 이진탐색 함수
    start = 0
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] == number:
            return 1
        elif lst[middle] > number:
            end = middle - 1
        else:
            start = middle + 1
    return 0


N = int(input())
lst = sorted(list(map(int, input().split())))
M = int(input())

for number in map(int, input().split()):
    if binarysearch(number, N-1):
        print(1)
    else:
        print(0)
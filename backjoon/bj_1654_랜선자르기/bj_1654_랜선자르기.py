import sys
sys.stdin = open('input.txt')


def cut(standard):
    cnt = 0
    for cable in lst:
        cnt += cable // standard
    return cnt

    
def binary_search(end):
    global maxlength
    start = 1

    while start <= end:
        middle = (start + end) // 2
        cnt = cut(middle)
        
        # 자른 케이블 수가 목표 치보다 같거나 많을 때
        if cnt >= N and maxlength < middle:
            maxlength = middle
            start = middle + 1
        
        # 자른 케이블 수가 목표 치보다 적을 때
        else:
            end = middle - 1



T = int(input())
for tc in range(1, T+1):
    K, N = map(int, input().split())
    lst = [int(input()) for _ in range(K)]
    # lst.sort()
    maxlength = 0
    # maxlength = idx = 0
    #
    # while idx < N-1 and cut(lst[idx]) >= N:
    #     maxlength = lst[idx]
    #     idx += 1

    binary_search(max(lst))
    print(maxlength)
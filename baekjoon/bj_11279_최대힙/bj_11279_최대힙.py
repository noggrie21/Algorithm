import sys
sys.stdin = open('input.txt')


def insert(num):
    global last
    last += 1
    heap[last] = num
    c = last
    p = c//2
    # print(p, c)
    while p and heap[p] < heap[c]: # 걸리는 부분 부모 존재 여부 확인
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2
        # print(heap)


def delete():
    global last
    result = heap[1]
    heap[1] = heap[last]
    heap[last] = 0
    last -= 1
    p = 1
    c1 = p*2
    c2 = c1+1
    # print(p, c1, c2, last)
    # print(heap)
    while c1 <= K and heap[p] < heap[c1]:
        # print(heap)
        if c2 <= K and heap[c1] < heap[c2]:
            # heap[p], heap[c2] = heap[c2], heap[p]
            c1 = c2
        if heap[p] < heap[c1]:
            heap[p], heap[c1] = heap[c1], heap[p]
        p = c1
        c1 = p*2
        c2 = c1+1
    return result


K = int(input())
heap = [0] * (K+1)
last = 0
for _ in range(K):
    num = int(input())
    if not num:
        if not heap[1]:
            print(0)
        else:
            print(delete())
    else:
        insert(num)




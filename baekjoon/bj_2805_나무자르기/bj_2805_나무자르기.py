def binary_search(end):
    start = 1
    maxV = 0
    while start <= end:
        middle = (start + end) // 2
        need = 0

        for tree in trees:
            if tree > middle:
                need += tree-middle
        # need = sum(map(lambda x: (0 if x <= middle else x - middle), trees))

        if need < M:
            end = middle - 1
        else:
            maxV = max(maxV, middle)
            start = middle + 1

    return maxV


N, M = map(int, input().split())
trees = list(map(int, input().split()))
print(binary_search(max(trees)))
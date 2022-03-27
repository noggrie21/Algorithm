import sys
sys.stdin = open('cinput.txt')

for tc in range(int(input())):
# def check(arr):
#     for i in range(1, N):
#         if abs(arr[i]-arr[i-1]) > K:
#             return False
#     return True
#
#
#
#
# def switch():
#     # 어떤 인덱스가 안맞는 지 보내주는 함수
#     # 해당 반환값으로 받은 인덱스 번호에 b값을 넣어보고
#     # 다시 어떤 인덱스가 안맞는지 보내주는 함수에 넣어
#     # - 또 뭐가 와 그러면 또 바꿔봐
#     # 근데 만약에 반환을 N으로 받으면,
#     # 그때는 이제 b로 바꿔서 다시 해
#     # - 만약에 반환값을 못받으면, 가능하다는 이야기로
#     # return 1
#     idx = old = 0
#     flag = 1
#     while flag:
#         i = find_idx(a, idx)
#         if idx == i:  # idx == i: b값으로 바꿨는데도 또 거기가 안맞는다고 왓어
#             break
#         a[i] = b[i]
#         idx = i
#
#

    def find_idx():
        global ai
        global bi

        if N == 1:
            return

        for i in range(N-1):
            if abs(a[i] - a[i+1]) > K:
                ai = i
                break

        for i in range(N-1):
            if abs(b[i] - b[i+1]) > K:
                bi = i
                break





    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 'No'
    ai = bi = N
    find_idx()
    print(ai, bi)


def DFS(i, n, end, lst):
    print(lst)
    if n == end:
        print('여긴 재귀의 끝')
        return 1
    elif 1 <= n <= end - 1:
        print('여긴 중간')
        if abs(lst[n] - lst[n - 1]) > K:
            print('k보다 크다')
            return

    if DFS(i + 1, n + 1, end, lst + [a[i]]):
        return 1
    if DFS(i + 1, n + 1, end, lst + [b[i]]):
        return 1



    if ai == N or bi == N:
        result = 'Yes'
    elif ai >= bi:
        a.append(0)
        b.append(0)
        if DFS(ai+1, 0, N-ai, a[:ai] + [b[ai]]) or DFS(bi+1, 0, N-bi, b[:bi] + [a[bi]]):
            result = 'Yes'
    else:
        a.append(0)
        b.append(0)
        if DFS(bi+1, 0, N-bi, b[:bi] + [a[bi]]) or DFS(ai+1, 0, N-ai, a[:ai] + [b[ai]]):
            result = 'Yes'

    print(result)

# X 배열의 특징
# 1. 길이가 N
# 2. 각 요소의 차이가 K보다 작거나 같아야함
# 3. 각 요소가 a와 b요소에 있어야 함

# def check(arr):
#     print(arr)
#     global result
#     for i in range(N+1):
#         cnt = 0
#         for j in range(i, i+N-1):
#             if abs(arr[j] - arr[j+1]) <= K:
#                 cnt += 1
#         print(cnt)
#         if cnt == N - 1:
#             result = 'Yes'
#             return



# x = a + b
# x.sort()
# check(x)

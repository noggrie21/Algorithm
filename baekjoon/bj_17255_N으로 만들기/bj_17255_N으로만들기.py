def DFS(n, lst, N):
    global answer
    global number
    # print(lst)


    if len(lst) == N:
        answer.add('/'.join(lst))
        return

    else:
        left = n - 1

        while 0 <= left < N and used[left]:
            left -= 1

        if 0 <= left < N:
            used[left] = 1
            DFS(left, lst + [number[left] + lst[-1]], N)
            used[left] = 0

        right = n + 1

        while 0 <= right < N and used[right]:
            right += 1

        if 0 <= right < N:

            used[right] = 1
            DFS(right, lst + [lst[-1] + number[right]], N)
            used[right] = 0



# 입력
number = input()

N = len(number)
used = [0] * N
answer = set()

for n in range(N):
    used[n] = 1
    DFS(n, [number[n]], N)
    used[n] = 0

# 출력
print(len(answer))
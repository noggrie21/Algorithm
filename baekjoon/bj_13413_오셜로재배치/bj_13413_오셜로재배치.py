T = int(input())


def settings(text):
    global result
    lst = [0] * N
    cnt = 0

    for i in range(N):
        if text[i] == 'W':
            lst[i] = 1
            cnt += 1
            result[i] += 1

    return lst, cnt


for tc in range(T):
    N = int(input())

    text1 = input()
    text2 = input()

    result = [0] * N

    initial, initial_cnt = settings(text1)
    target, target_cnt = settings(text2)

    answer = 0

    mixed = result.count(1)
    if mixed:
        if initial_cnt == target_cnt:
            answer = mixed // 2
        else:
            answer = (mixed - abs(initial_cnt - target_cnt)) // 2 + abs(initial_cnt - target_cnt)
    print(answer)




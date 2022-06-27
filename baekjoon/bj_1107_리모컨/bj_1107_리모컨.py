def check(N, length, number, start, end):
    global cnt

    # 최대한 그냥 누를 수 있는 번호 눌러놓기
    for i in range(length):
        if rc[int(N[i])]:
            cnt += 1
        else:
            N = N[i:]
            break
    # print(cnt, N) OK

    # 다 눌러버렸다면 함수 종료
    if cnt == length:
        return

    # 못누른 숫자가 있다면,
    bigger = smaller = 1000000
    char = int(N[0])
    plus, minus = char + 1, char - 1

    # 못누른 숫자에서 누를 수 있는 큰 수의 최솟값 찾기
    while plus < 10:
        if rc[plus]:
            bigger = plus
            break
        plus += 1

    if bigger != 1000000:
        bigger = int(f'{bigger}' + f'{start}' * (length - cnt - 1))
    # print(bigger)

    # 못누른 숫자에서 누를 수 있는 작은 수의 최댓값 찾기
    while 0 <= minus:
        if rc[minus]:
            smaller = minus
            break
        minus -= 1

    if smaller != 1000000:
        smaller = int(f'{smaller}' + f'{end}' * (length - cnt - 1))
    # print(smaller)

    # 누를 수 있는 숫자들 중에 찾는 채널과 가장 가까운 수 고르기
    # print(f'bigger: {bigger}, smaller: {smaller}')
    # print(f'number:{number}')
    N = int(N)
    diff = min(abs(bigger-N), abs(smaller-N))
    # print(number, diff)
    # 누른 횟수 카운팅하기
    # print(f'diff:{diff}')
    cnt += (length - cnt - 1 + diff)


N = input()
M = int(input())

length = len(N)
cnt = 0
now = 100
number = int(N)

if not M:
    # print('61', length)
    print(length)

elif now == number:
    dump = list(map(int, input().split()))
    # print('65', cnt)
    print(cnt)
else:
    broken = list(map(int, input().split()))
    rc = [1] * 10
    start = 10
    end = -1

    for i in range(10):
        if i in broken:
            rc[i] = 0
        else:
            start = min(start, i)
            end = max(end, i)

    if start * end < 0:
        print(abs(number-now))
    else:
        check(N, length, number, start, end)
        # print('81',cnt)
        print(cnt)
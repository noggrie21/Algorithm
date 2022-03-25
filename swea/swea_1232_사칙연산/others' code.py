def calc(n):
    if type(values[n]) != type('a'):
        return values[n]
    else:
        if values[n] == '+':
            return calc(ch1[n]) + calc(ch2[n])
        elif values[n] == '-':
            return calc(ch1[n]) - calc(ch2[n])
        elif values[n] == '*':
            return calc(ch1[n]) * calc(ch2[n])
        elif values[n] == '/':
            return calc(ch1[n]) / calc(ch2[n])


for tc in range(1, 11):
    n = int(input())

    values = [0] * (n + 1)
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)

    for _ in range(n):
        lst = input().split()
        idx = int(lst[0])

        if len(lst) == 2:
            values[idx] = int(lst[1])
        else:
            values[idx] = lst[1]
            ch1[idx] = int(lst[2])
            ch2[idx] = int(lst[3])

    result = int(calc(1))
    print(f'#{tc}', result)
N = int(input())
lst = [0, 1, 2, 0]
i = 3
if N == 1:
    print(1)
elif 2 <= N < 8:
    print(2)
else:
    while True:
        lst[i] = lst[i-1] + 6*(i-2)
        if lst[i] < N:
            i += 1
            lst.append(0)
            continue
        elif lst[i] > N:
            print(i-1)
            break
        else:
            print(i)
            break

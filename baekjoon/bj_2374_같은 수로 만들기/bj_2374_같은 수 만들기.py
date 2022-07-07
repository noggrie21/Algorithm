def divide(lst):
    global add
    print(lst)

    if len(lst) == 1:
        return lst[0]

    else:
        standard = lst.index(max(lst))
        print(standard)

        add += lst[standard] - divide(lst[:standard])

        print(1, lst[standard])
        add += lst[standard] - divide(lst[standard+1:])

        return lst[standard]


N = int(input())

numbers = list(int(input()) for _ in range(N))
add = 0
divide(numbers)
print(add)
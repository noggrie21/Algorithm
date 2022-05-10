def fibo(n):
    global zero
    global one

    if n <= 1:
        if n == 1:
            one += 1
        else:
            zero += 1
        return n

    else:
        return fibo(n-1) + fibo(n-2)


for _ in range(int(input())):
    n = int(input())
    zero = one = 0
    fibo(n)
    print(zero, one)
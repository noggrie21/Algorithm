from sys import stdin

N = int(input())
lst = []

for _ in range(N):
    command, *X = stdin.readline().rstrip().split()

    if command == 'push':
        lst.append(int(*X))

    elif command == 'pop':
        if not lst:
            print(-1)
        else:
            print(lst.pop())

    elif command == 'size':
        print(len(lst))

    elif command == 'empty':
        if not lst:
            print(1)
        else:
            print(0)

    else:
        if not lst:
            print(-1)
        else:
            print(lst[-1])

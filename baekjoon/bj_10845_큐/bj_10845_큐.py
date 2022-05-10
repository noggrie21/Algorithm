from sys import stdin

N = int(input())
queue = ['' for _ in range(N)]
front = 0
rear = 0

for _ in range(N):
    command, *X = stdin.readline().rstrip().split()
    char = command[-1]
    # print(command, end='')

    if char == 'h':
        queue[rear] = X[0]
        rear += 1

    elif char == 'p':
        if front == rear:
            print(-1)
        else:
            print(queue[front])
            front += 1

    elif char == 'e':
        print(rear-front)

    elif char == 'y':
        if front == rear:
            print(1)
        else:
            print(0)

    elif char == 't':
        if front == rear:
            print(-1)
        else:
            print(queue[front])

    elif char == 'k':
        if front == rear:
            print(-1)
        else:
            print(queue[rear-1])



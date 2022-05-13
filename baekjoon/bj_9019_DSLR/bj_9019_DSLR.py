from sys import stdin


def DSLR(num):
    word = f'{num:04d}'
    result = {
        'D': (num*2)%10000,
        'S': num+9999-bool(num)*10000,
        'L': int(word[1:]+word[0]),
        'R': int(word[-1]+word[:3])
    }
    return result


def bfs(start, end):
    q = ['' for _ in range(10000)]
    visited = ['' for _ in range(10000)]
    front = -1
    rear = 0
    q[rear] = start
    visited[start] = 'start'
    cnt = 0

    while front != rear:
        front += 1
        num = q[front]

        for command, new in DSLR(num).items():

            if new == end:
                return visited[num][5:]+command

            if not visited[new]:
                cnt += 1
                rear += 1
                q[rear] = new
                visited[new] = visited[num] + command


T = int(input())
for _ in range(T):
    initial, target = map(int, stdin.readline().rstrip().split())
    print(bfs(initial, target))
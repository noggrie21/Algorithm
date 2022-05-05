from sys import stdin

def bfs(v):
    vistied = [0] * (N+1)
    vistied[v] = 1
    q = [0] * N
    front = -1
    rear = 0
    q[rear] = v

    while front != rear:
        front += 1
        v = q[front]

        for new in arr[v]:
            if not vistied[new]:
                rear += 1
                q[rear] = new
                vistied[new] = 1

    return rear


N = int(input())
E = int(input())

arr = [[] for _ in range(N+1)]

for _ in range(E):
    v1, v2 = map(int, stdin.readline().rstrip().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

print(bfs(1))
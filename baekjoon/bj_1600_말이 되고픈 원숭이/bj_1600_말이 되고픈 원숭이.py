def bfs():
    q = [[0,  0]]
    visited = [[0]*W for _ in range(H)]
    visited[0][0] = 1

K = int(input())
W, H = map(int, input().split())

zoo = [list(map(int, input().split())) for _ in range(H)]
answer = bfs()
print(zoo)
def BFS(start):
  visited = [0] * 100001
  q = [start]
  visited[start] = 1

  while q:
    now = q.pop(0)

    for next, time in [(now*2,visited[now]), (now-1,visited[now]+1), (now+1, visited[now]+1)]:
      if 0 <= next <= 100000 and (not visited[next] or (visited[next] and time < visited[next])):

        visited[next] = time

        if next == K:
          return visited[next] - 1

        q.append(next)

N, K = map(int,input().split())

print(BFS(N))
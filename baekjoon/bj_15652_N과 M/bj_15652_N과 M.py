def DFS(n, lst, start=1):
  # 종료 파트
  if n >= M:
    print(*lst)
    return

  # 유도 파트
  for i in range(start, N+1):
    DFS(n+1, lst + [i], i)

N, M = map(int, input().split())

DFS(0, [])
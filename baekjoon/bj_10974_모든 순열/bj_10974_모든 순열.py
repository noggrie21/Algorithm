def nPn(n, lst):
    # 종료조건
    if n >= N:
      print(*lst)
      return

    # 유도조건
    for i in range(N):
      if not used[i]:
        used[i] = 1
        nPn(n+1, lst+[number[i]])
        used[i] = 0
    return

N = int(input())
used = [0] * N
number = list(range(1, N+1))
nPn(0, [])



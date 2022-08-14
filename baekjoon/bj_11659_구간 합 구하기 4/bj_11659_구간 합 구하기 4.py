import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))
prefix = [0]*N
prefix[0] = numbers[0]

for i in range(1, N):
  prefix[i] = numbers[i] + prefix[i-1]

prefix = [0] + prefix

for _ in range(M):
  start, end = map(int, sys.stdin.readline().rstrip().split())

  print(prefix[end] - prefix[start-1])
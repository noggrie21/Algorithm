import sys

N = int(input())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())

prefix = [0] * N
prefix[0] = numbers[0]

for i in range(1, N):
  prefix[i] = prefix[i-1] + numbers[i]
prefix = [0] + prefix

for _ in range(M):
  i, j = map(int, input().split())
  print(prefix[j]-prefix[i-1])

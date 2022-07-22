import sys

N, M = map(int, input().split())
words = set(sys.stdin.readline().rstrip() for _ in range(N))

answer = 0

for _ in range(M):
    if words.intersection({sys.stdin.readline().rstrip()}):
        answer += 1

print(answer)





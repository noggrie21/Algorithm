import sys
sys.stdin = open('input (1).txt')

for tc in range(1, 11):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]



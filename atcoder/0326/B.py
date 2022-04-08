N = int(input())
lst = list(map(int, input().split()))

for i in range(2001):
    if i not in lst:
        print(i)
        break
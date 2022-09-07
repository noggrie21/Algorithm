import sys
sys.setrecursionlimit(1003)


def add(i, num, cnt, total):
    global a
    global b

    if i == A-1:
        a = total + num

    if i == B+1:
        b = total
        return

    if num == cnt:
        add(i+1, num+1, 1, total+num)
    else:
        add(i+1, num, cnt+1, total+num)


A, B = map(int, input().split())
a = b = 0
add(1, 1, 1, 0)

print(b-a)

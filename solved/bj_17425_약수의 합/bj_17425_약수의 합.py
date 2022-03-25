# a = bc
# c를 a의 약수
# f(a) = a의 모든 약수를 더한 값
# g(x) = x보다 작거나 같은 모든 자연수 y의 f(y)를 더한 값

# g(
import sys
sys.stdin = open('input.txt')


def f(x):
    f_total = 0
    for i in range(1, x+1):
        if not x % i:
            f_total += i
    return f_total


def g(y):
    g_total = 0
    for i in range(1, y+1):
        g_total += f(i)
    return g_total

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = g(N)
    print(f'{result}')


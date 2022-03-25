import sys
sys.stdin = open('input (1).txt')


def set_relation(data):
    idx = int(data[0])
    n = len(data)
    if n > 2:
        tree[idx] = data[1]
        child[idx][0] = int(data[2])
        child[idx][1] = int(data[3])
    else:
        tree[idx] = int(data[1])


def post_order(v):
    if isinstance(tree[v], int):
        return tree[v]
    num1 = post_order(child[v][0])
    num2 = post_order(child[v][1])
    return calculate(tree[v], num1, num2)


def calculate(value, num1, num2):
    if value == '+':
        return num1 + num2
    elif value == '-':
        return num1 - num2
    elif value == '*':
        return num1 * num2
    else:
        return num1 / num2


operator = '+-*/'

for tc in range(1, 11):
    N = int(input())
    child = [[0, 0] for _ in range(N + 1)]
    tree = [0] * (N + 1)

    for _ in range(N):
        data = input().split()
        set_relation(data)

    ans = post_order(1)
    print(f'#{tc}', int(ans))

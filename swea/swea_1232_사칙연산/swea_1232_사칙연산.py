import sys
sys.stdin = open('input (1).txt')


def int_(char):
    if char.isdecimal():
        return int(char)
    else:
        return char


def set_child():
    for i in range(2, len(data)):
        if not child[data[0]][0]:
            child[data[0]][0] = data[i]
        else:
            child[data[0]][1] = data[i]


def post_order(v):
    if v:
        post_order(child[v][0])
        post_order(child[v][1])
        post_calculate(tree[v])


def post_calculate(value):
    if isinstance(value, int):
        stack.append(value)
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        result = calculate(value, num1, num2)
        stack.append(result)


def calculate(value, num1, num2):
    if value == '+':
        return num1 + num2
    elif value == '-':
        return num1 - num2
    elif value == '*':
        return num1 * num2
    else:
        return num1 / num2


for tc in range(1, 11):
    N = int(input())
    child = [[0, 0] for _ in range(N + 1)]
    tree = [0] * (N + 1)
    for _ in range(N):
        data = list(map(int_, input().split()))
        tree[data[0]] = data[1]
        set_child()
    stack = []
    post_order(1)
    print(f'#{tc}', int(stack[0]))



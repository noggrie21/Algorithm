def postfix(notation):
    stack = []

    for elem in notation:
        if elem not in "+-/*":
            stack.append(alpha_to_num[ord(elem)-ord('A')])
        else:
            num2, num1 = stack.pop(), stack.pop()
            stack.append(calculate(num1, num2, elem))

    return stack[0]


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        return num1 / num2


N = int(input())

notation = input()

alpha_to_num = [int(input()) for _ in range(N)]

print(f'{postfix(notation):.2f}')




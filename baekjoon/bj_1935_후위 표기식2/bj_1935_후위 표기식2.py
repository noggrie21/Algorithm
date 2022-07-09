def postfix(notation):
    stack = []

    # 후위 표기식에서 하나씩 순회하면서
    for elem in notation:

        # 피연산자일 경우,
        # stack에 삽입
        if elem not in "+-/*":
            stack.append(alpha_to_num[ord(elem)-ord('A')])

        # 연산자일 경우,
        # stack에 최근에 담긴 피연산자 2개를 뽑아 연산 후 삽입
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




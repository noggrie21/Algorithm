


# import re
# from functools import reduce
#
#
# def calculate(expression):
#     i = 0
#     stack = []
#
#     while i < len(expression):
#         if expression[i] == '+':
#             stack.append(stack.pop() + expression[i + 1])
#             i += 1
#         elif isinstance(expression[i], int):
#             stack.append(expression[i])
#         i += 1
#
#     ans = reduce(lambda x, y: x-y, stack)
#     return ans
#
#
# expression = list(map(lambda x: int(x) if x.isdecimal() else x, re.split('([+|-])', input())))
# print(calculate(expression))
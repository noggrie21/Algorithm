from functools import reduce

numbers = [-1, 2, 3, 4, 5]
total = reduce(lambda acc, cur: acc+abs(cur), numbers)
print(total)

def append_remaint(array):
    if len(array) % 2:
        minimum = array.pop()

        if minimum < 0 and 0 in add_list:
            return []

        return [minimum]

    return []


def bind(array):
    result = 0

    for i in range(0, len(array), 2):
        result += array[i] * array[i+1]

    return result


N = int(input())

negative = []
positive = []
add_list = []

for _ in range(N):
    number = int(input())

    if number < 0:
        negative.append(number)

    elif not number or number == 1:
        add_list.append(number)

    else:
        positive.append(number)

negative.sort()
positive.sort(reverse=True)

add_list += append_remaint(negative)
add_list += append_remaint(positive)

answer = sum(add_list) + bind(negative) + bind(positive)
print(answer)

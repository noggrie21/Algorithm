def mode(numbers):
    maxC = maxV = 0
    for number in set(numbers):
        cnt = numbers.count(number)
        if maxC < cnt:
            maxC = cnt
            maxV = number
        elif maxC == cnt and maxV < number:
            maxV = number
    return maxV



N = int(input())
numbers = []
total = 0

for _ in range(N):
    number = int(input())
    total += number
    numbers.append(number)

numbers.sort()
print(f'{round(total/N)}')
print(numbers[N//2])
print(mode(numbers))
print(numbers[-1]-numbers[0])

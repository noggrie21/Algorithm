students = [0] * 31

for _ in range(28):
    num = int(input())
    students[num] = 1

for num in range(1, 31):
    if not students[num]:
        print(num)
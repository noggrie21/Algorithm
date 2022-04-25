num = 1
for _ in range(3):
    num *= int(input())

counts = [0] * 10

while num:
    temp = num % 10
    counts[temp] += 1
    num //= 10

print("\n".join(map(str, counts)))

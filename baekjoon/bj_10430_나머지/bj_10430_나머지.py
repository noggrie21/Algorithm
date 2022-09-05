A, B, C = map(int, input().split())

first =  (A + B) % C
second = ((A % C) + (B % C)) % C
third = (A * B) % C
forth = ((A % C) * (B % C)) % C

print(first)
print(second)
print(third)
print(forth)
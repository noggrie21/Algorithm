ban = int(input())
cars = list(map(int, input().split()))

print(len(list(filter(lambda x: x == ban, cars))))
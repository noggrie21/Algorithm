people = 0
max_people = 0

for _ in range(10):
    off, on = map(int, input().split())

    people += (on - off)

    max_people = max(max_people, people)

print(max_people)

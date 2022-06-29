N = int(input())
files = [list(input()) for _ in range(N)]
# print(files)
answer = []

for i in range(len(files[0])):
    check = set()

    for j in range(N):
        check.add(files[j][i])

    if len(check) == 1:
        answer.append(files[j][i])
    else:
        answer.append('?')

print("".join(answer))
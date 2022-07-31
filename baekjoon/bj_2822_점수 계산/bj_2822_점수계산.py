
scores = list((i, int(input())) for i in range(1, 9))
scores.sort(key=lambda x:x[1], reverse=True)
# print(scores)
total = 0
answer = []

for i in range(5):
  answer.append(scores[i][0])
  total += scores[i][1]

print(total)
print(*sorted(answer))


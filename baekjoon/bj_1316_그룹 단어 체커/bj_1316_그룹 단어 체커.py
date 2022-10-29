N = int(input())

cards = list(range(1, N+1))

for i in range(N):
  print(cards.pop(0))
  cards.
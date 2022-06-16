N = int(input()) # N: 유제품의 수

items = [] # items: 유제품 가격이 담길 배열

for _ in range(N):
    items.append(int(input()))

items.sort(reverse=True)

cost = 0

for inx, item in enumerate(items):
    if inx % 3 == 2: # 무료 처리하기
        continue
    cost += item

print(cost)
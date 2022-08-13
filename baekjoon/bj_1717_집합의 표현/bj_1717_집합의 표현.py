def find(a, b):
    while num[a] != a:
      a = num[a]

    while num[b] != b:
      b = num[b]
    
    if b == a:
        return 'YES'
    return 'NO'

def union(a, b):
    # a의 대장찾기
    while a != num[a]:
      a = num[a]
    
    num[b] = a
    return


N, M = map(int, input().split())

num = list(range(N+1))
# print(num)

for _ in range(M):
  flag, a, b = map(int, input().split())

  if a > b:
    a, b = b, a

  if flag:
    # print(num)
    print(find(a, b))
    continue
  
  union(a, b)

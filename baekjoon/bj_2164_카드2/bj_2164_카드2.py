from collections import deque

N = int(input())
q = deque()
q.extend(list(range(1, N+1)))

while len(q) >= 2:
    # 버리기
    q.popleft()
    # 맨 앞장 빼서 맨 뒤로 넣기
    q.append(q.popleft())

print(q.popleft())
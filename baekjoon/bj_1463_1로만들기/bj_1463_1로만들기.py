from collections import deque

# 주석 처리된 q는 deque를 사용하지 않고, list의 pop 메소드 사용
# queue는 deque를 import해서 사용

def bfs(start):
    '''

    '''
    # q = [start]
    queue = deque()
    queue.append(start)
    visited = [0]*(10**6+1)
    visited[start] = 1

    while queue:
        # current = q.pop(0)
        current = queue.popleft()
        if current == 1:
            return visited[current] - 1

        for new, check in [(current // 3, current % 3), (current // 2, current % 2), (current - 1, 0)]:
            if not check and not visited[new]:
                # q.append(new)
                queue.append(new)
                visited[new] = visited[current] + 1


number = int(input())
print(bfs(number))
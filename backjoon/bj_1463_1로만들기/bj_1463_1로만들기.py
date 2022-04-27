from collections import deque


def bfs(start):
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

        for new, check in [(current//3, current%3), (current//2, current%2), (current-1, 0)]:
            if not check and not visited[new]:
                # q.append(new)
                queue.append(new)
                visited[new] = visited[current] + 1


number = int(input())
print(bfs(number))
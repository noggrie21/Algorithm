# from collections import deque

def bfs(v):
    queue = [0] * (N+1)                             # queue는 (N - 설탕배달 가능 무게의 조합)이 담길 배열(길이는 넉넉히 하기 위해 N+1로)
    visited = [0] * (N+1)                           # (N - 설탕배달 가능 무게의 조합)의 중복을 확인하고, 봉지 갯수를 기록할 배열
    front = -1                                      # queue에서 pop연산을 위한 인덱스로 활용
    rear = 0                                        # queue에서 append연산을 위한 인덱스로 활용
    queue[rear] = v                                 # queue 초기값 삽입
    visited[v] = 0

    while front != rear:                            # queue가 빌 때까지(front == rear)
        front += 1                                  # pop연산을 위해 front += 1
        v = queue[front]

        if v == 0:                                  # 남은 설탕이 없다면
            return visited[v]                       # (설탕배달이 가능다는 것으로) 봉지 갯수 반환

        for number in [v-3, v-5]:                   # 아직 남은 설탕이 있다면, 3kg 혹은 5kg 배달해보기
            if 0 <= number and not visited[number]: # 남은 설탕양이 유효한 값이면서(0<=number), 기존에 배달한 적 있는 설탕 무게가 아니라면
                visited[number] = visited[v] + 1    # 봉지 갯수 기록
                rear += 1                           # queue에 삽입하기
                queue[rear] = number

    return -1


N = int(input())
print(bfs(N))

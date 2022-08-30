def DFS(r, my, team):
    # 종료 파트
    if r >= 5:
        return True

    # 유도 파트
    for friend in relations[my]:
        if not used[friend]:
            used[friend] = 1
            if DFS(r+1, friend, team + [friend]):  # 특정 관계를 만족하는 경우 발견 시 바로 탐색 종료
                return True
            used[friend] = 0


def beFriends(M):
    relations = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        relations[b].append(a)
        relations[a].append(b)

    return relations


# 입력 받기
N, M = map(int, input().split())

relations = beFriends(M)  # relations : 인접 리스트

answer = 0
used = [0] * N

for i in range(N):
    if relations[i] and DFS(0, i, []):  # 친구가 존재하는 경우에, DFS 탐색시작
        answer = 1
        break

# 출력 하기
print(answer)


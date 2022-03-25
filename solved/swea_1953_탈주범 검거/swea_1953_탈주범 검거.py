import sys
sys.stdin = open('sample_input.txt')

# 출력 : 탈주범이 위치할 수 있는 장소의 개수
# 탈주범은 1시간에 1거리 이동
# 지하터널의 크기 세로 N, 가로 M (5 <= N, M <= 50)
# 맨홀 뚜껑 (R, C)
# 소요시간 : L (1 <= L <= 20)
# L = 1일때, 탈주범위 위치 = (R , C)
# 지하 터널 지도에는 반드시 1개 이상의 터널이 있음
# 맨홀은 터널 위치에 존재


# 델타순서: 상, 우, 하, 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# types = {번호: 델타배열의 인덱스로 가능한 값}
# 예를들면,
# key = 1인 경우, value = [0, 1, 2, 3]이므로 <상, 우, 하, 좌>방향으로 이동가능
# key = 3인 경우, value = [1, 3]이므로 <우, 좌>방향으로 이동가능
types = {
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [1, 3],
    4: [0, 1],
    5: [1, 2],
    6: [2, 3],
    7: [0, 3]
}


def bfs(R, C):
    queue = [(R, C)]
    visited[R][C] = 1
    cnt = 1
    while queue:
        i, j = queue.pop(0)
        if visited[i][j] == L:
            break
        for k in types.get(tunnel[i][j]):
            ni, nj = i + di[k], j + dj[k]
            if not visited[ni][nj] and\
                tunnel[ni][nj] and (k+2) % 4 in types[tunnel[ni][nj]]:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                cnt += 1
    return cnt


T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    # tunnel : 인덱스 범위 확인 절차 생략을 위한 테두리 둘러서 입력 받기
    tunnel = [[0] * (M+2)] +\
             [[0] + list(map(int, input().split())) + [0] for _ in range(N)] +\
             [[0] * (M+2)]
    visited = [[0] * (M+2) for _ in range(N+2)]
    # R, C는 테두리를 염두해서 +1씩 넣어주기
    ans = bfs(R+1, C+1)
    print(f'#{tc} {ans}')

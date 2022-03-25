import sys
sys.stdin = open('sample_input.txt')
# 이동방향 1: 상, 2: 하, 3: 좌, 4: 우
# 1. 1시간마다 이동 방향 다음셀로 이동
# 2. 남은 미생물 수 //= 2
# 3. 이동 후 같은 위치 셀이 있는 경우 군집 합쳐지고, 원래 더 많은 미생물을 가졌던 군집의 방향 상속


T = int(input())
delta = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]              # delta: 미생물이 가진 방향 정보를 인덱스로 하는 리스트
converter = [0, 2, 1, 4, 3]                                 # converter: 약품에 닿았을 때 방향을 반전시키기 위한 리스트
                                                            # (예: 기존 1이면(상방향) converter[1] = 2(하방향)


def spend(N, M, K):
    idx = list(range(K))                                    # idx: micro를 순회할 인덱스가 들어있는 리스트

    while M:
        visited = {}                                        # visited: {(nr, nc) : 해당 미생물의 idx}
        removals = []                                       # removals: 사라질 미생물의 idx가 담길 리스트
        overlap = set()                                     # overlap: 중복 위치가 담길 셋

        # idx를 인덱스로 하여 micro 순회하기
        for i in idx:
            nr = micro[i][0] + delta[micro[i][3]][0]
            nc = micro[i][1] + delta[micro[i][3]][1]        # 새로 이동할 좌표가

            if nr in [0, N-1] or nc in [0, N-1]:            # 1. 약품이 묻어있는 경우
                micro[i][2] //= 2                           # 미생물을 반으로 죽이고
                if not micro[i][2]:                         # 만약에 미생물 수가 0이면
                    removals.append(i)                      # removals에 추가
                micro[i][3] = converter[micro[i][3]]        # 방향 전환받기

            elif (nr, nc) not in visited:                   # 2. visited에 없는 좌표면
                visited[(nr, nc)] = [i]                     # {좌표: [해당 인덱스]} 쌍 추가

            else:                                           # 3. 이미 visited안에 존재하는 좌표면
                visited[(nr, nc)] += [i]                    # value(해당 인덱스) 추가
                overlap.add((nr, nc))                       # 중복 좌표 정보를 담는 overlap에 해당 좌표 넣기

            micro[i][0] = nr                                # 미생물 좌표 갱신
            micro[i][1] = nc

        # micro 순회가 한 번 끝나면 overlap과 removals 처리

        # overlap 처리
        for r, c in overlap:                                # 중복 좌표를 하나씩 꺼내서
            temp = []

            for i in visited[(r, c)]:                       # 같은 위치에 모인 미생물들의
                temp.append(micro[i][2])                    # 미생물 수를 temp에 넣고
            maxV = max(temp)                                # 가장 많은 미생물 수 찾기(뭉쳐지는 기준이 됨)

            for j in visited[(r, c)]:                       # 한번 더 순회하면서
                if micro[j][2] != maxV:                     # 기준(최댓값)과 다르면
                    removals.append(j)                      # removals에 등록
                else:                                       # 기준(최댓값)과 일치하면
                    micro[j][2] = sum(temp)                 # 미생물 수 합산으로 갱신

        # removal 처리
        for removal in removals:
            idx.remove(removal)                             # micro를 순회할 인덱스 제거하기

        M -= 1
    return idx


for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N: 셀의 개수, M: 격리 시간, K: 미생물 군집의 개수
    micro = [list(map(int, input().split())) for _ in range(K)]
    total = 0
    alive = spend(N, M, K)  # spend함수를 통해 살아남은 미생물의 인덱스가 담긴 리스트를 받음
    for i in alive:
        total += micro[i][2]
    print(f'#{tc} {total}')
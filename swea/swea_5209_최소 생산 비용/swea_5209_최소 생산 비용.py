import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def DFS(factory, total, pick):  # factory: 공장 번호 / total: 현재까지의 생산 비용 / pick: 선택된 상품번호가 담긴 리스트
    global ans

    # 가지치기
    if ans < total:                                                            # 현재까지의 생산비용이 ans보다 커지면 탐색 종료
        return

    # 기저파트
    if factory >= N and total < ans:                                           # 모든 공장이 상품을 선택했을때, 더 작은 비용을 찾으면
        ans = total                                                            # 최소 비용 갱신

    # 유도파트
    else:
        for product in range(1, N+1):                                          # 1부터 N까지 상품번호를 순회하면서
            if product not in pick:                                            # 선택되지 않은 상품이 있으면
                DFS(factory+1, total+cost[product][factory], pick+[product])   # total에 해당 상품 비용 더하고, pick에 추가해서 다음 함수 호출하기


for tc in range(1, T+1):
    N = int(input())
    cost = [[0] * N] + [list(map(int, input().split())) for _ in range(N)]

    '''
    상품번호를 인덱스로 그대로 쓰기위해 패딩 붙여서 입력 받기
    
    cost = [[0, 0, 0],
            [73, 21, 21],
            [11, 59, 40],
            [24, 31, 83]]
    '''

    ans = N * 99                                                                # 제품 수 * 최대 생산 비용으로 초기화
    DFS(0, 0, [])
    print(f'#{tc} {ans}')
import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def DFS(n, one, three):         # n: (n+1)월, one: 1개월이 시작되는 지점, three: 3개월이 시작되는 지점
    global ans
    if n > 11:
        total = len(three) * months       # total: (3달 이용권 요금 * 3개월로 시작될 지점의 갯수)로 초기화
        for i in one:
            temp = min(day * plan[i], month * bool(plan[i])) # (1일 이용권 요금, 1달 이용권 요금) 중 최솟값으로
            total += temp       # total에 합산
        if total < ans:         # ans보다 작을 때
            ans = total         # ans 갱신
        return
    DFS(n+1, one + [n], three)
    DFS(n+3, one, three + [n])


for tc in range(1, T + 1):
    day, month, months, year = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    ans = year      # 1년 이용권 금액으로 초기화
    DFS(0, [], [])
    print(f'#{tc} {ans}')


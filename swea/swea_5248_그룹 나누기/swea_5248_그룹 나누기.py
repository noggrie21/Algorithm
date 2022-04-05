import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())


# 스스로 대표자 되기
def make_set(N):
    lst = [0] * (N + 1)
    for i in range(1, N+1):
        lst[i] = i
    return lst


# 대표자 찾기
def find_set(a):
    while people[a] != a:
        a = people[a]
    return a


# y의 대표자를 x의 대표자로 바꾸기
def union(x, y):
    people[find_set(y)] = find_set(x)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    m = list(map(int, input().split()))
    ans = 0

    # 본인을 조의 대표자로 지목하도록 초기 세팅하기
    people = make_set(N)

    # 종이에 언급된 번호끼리 한 조로 묶어주기
    for i in range(M):
        union(m[i*2], m[i*2+1])

    # 대표자가 몇 명인지 카운트
    for i in range(1, N+1):
        if people[i] == i:
            ans += 1

    print(f'#{tc} {ans}')
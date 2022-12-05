'''
벨트 위 같은 종류의 초밥이 둘 이상 있을 수 있음
1. 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
2. 각 고객에게 초밥의 종류가 하나 쓰인 쿠폰을 발행하고,
    1번 행사에 참가할 경우 -> 쿠폰에 적힌 초밥 하나 무료 제공
    이 번호에 적힌 초밥이 없는 경우 요리사가 만들어줌

N == k : set(sushi) + set.add(c)
k < N : 하나씩 돌아봐야할듯..?
근데 누적합처럼 처음에 갯수 구하고 앞에꺼 빼고 뒤에꺼 더하고
현재 상황에서 counter[c]가 0이면 +1하고 1이면 걍 지금 종류수
최댓값일때 갱신하기
'''
from collections import Counter

# N: 접시 수 / d: 초밥의 가짓 수 / k: 연속해서 먹는 접시 수 / c: 쿠폰 번호
N, d, k, c = map(int, input().split())
sushi = list(int(input()) for _ in range(N))
sushi = sushi + sushi[:k-1]


# 스타트지점
part = Counter(sushi[:k])
answer = 0
types = len(part)


# 순차적으로 돌기
for start in range(N-1):
    coupon = 0

    # 앞에 스시 빼기
    part[sushi[start]] -= 1
    if not part[sushi[start]]:
        types -= 1

    # 뒷 스시 넣기
    if not part[sushi[start+k]]:
        types += 1
    part[sushi[start+k]] += 1

    # 좋은 쿠폰인지
    if not part[c]:
        coupon = 1

    if answer < types + coupon:
        answer = types + coupon

print(answer)

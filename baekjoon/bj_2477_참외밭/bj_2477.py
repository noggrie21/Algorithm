kmelon = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]
sides = list(map(lambda n: n[1], arr))                   # [50, 160, 30, 60, 20, 100]
max_even = 0                                             # 짝수 항 가장 긴 변 구하기
max_odd = 0                                              # 홀수 항 가장 긴 변 구하기
for i in range(6):
    if i % 2:
        if max_odd < sides[i]:
            max_odd = sides[i]
    else:
        if max_even < sides[i]:
            max_even = sides[i]

area = max_odd * max_even                                # 참외밭 전체 넓이 구하기
i = 0                                                    # 가짜밭 넓이 구하기
s_area = 0
while not s_area:
    if sides[(i % 6)] * sides[(i + 1) % 6] == area:      # 가장 긴 변 두개가 연속으로 나오면
        s_area = sides[(i + 3) % 6] * sides[(i + 4) % 6] # 하나를 건너 뛴 다음값부터 가짜 땅의 변의 길이가 된다.
    else:
        i += 1
print((area-s_area)*kmelon)
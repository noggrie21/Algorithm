ans = ["right", "wrong"]

powers = [0] * 30001                                    # powers[숫자] = 숫자의 2제곱
for i in range(1, 30001):
    powers[i] = i**2

while True:
    numbers = sorted(list(map(int, input().split())))   # 오름차순 정렬(numbers[-1]이 빗변)
    x, y, z = map(lambda x: powers[x], numbers)         # 피타고라스 정리 이용하기 위해 2제곱 값으로 변환
    if not x + y + z:                                   # (0, 0, 0)인 경우
        break                                           # while 종료
    elif not x + y - z:                                 # (0, 0, 0)이 아니면서 x + y = z일 때(=직각 삼각형)
        print(ans[0])
    else:                                               # (0, 0, 0)이 아니면서 x + y != z일 때(=직각 삼각형이 아닐 때)
        print(ans[1])

import sys
sys.stdin = open('sample_input.txt', 'r')


def simulate():
    lst = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            distance = gradient(atom[i], atom[j])   # 두 원자가 부딪힐 수 있으면 distance = 충돌 지점과 원자들의 거리의 합, 부딪히지 않으면 distance = None
            if distance:                            # distance가 유효한 값이라면
                lst.append([distance / 2, i, j])    # distance / 2: 충돌 지점과의 거리, 어떤 원자가 충돌하는 지를 lst에 추가
    return lst


def gradient(arr1, arr2):
    x = arr1[0] - arr2[0]
    y = arr1[1] - arr2[1]

    # 두 원자의 기울기가 0, 1, -1인 경우에만 부딪힐 수 있기 때문에,
    # 기울기를 먼저 확인하고 정말 부딪힐 수 있는 방향인지 check_diretion함수를 통해 확인받는다.

    # 기울기가 0인 경우(Y축과 수평)
    if not x:
        if check_diretion(0, x, y, arr1, arr2):
            return abs(y)

    # 기울기가 0인 경우(X축과 수평)
    elif not y:
        if check_diretion(0, x, y, arr1, arr2):
            return abs(x)

    # 기울기가 1인 경우
    elif x / y == 1:
        if check_diretion(1, x, y, arr1, arr2):
            return abs(x)+abs(y)

    # 기울기가 -1인 경우
    elif x / y == -1:
        if check_diretion(-1, x, y, arr1, arr2):
            return abs(x)+abs(y)

    # 부딪힐 확률이 전혀 없는 경우
    else:
        return


def check_diretion(m, x, y, arr1, arr2):
    d1, d2 = arr1[2], arr2[2]

    # 기울기 = 0
    if not m:
        # y축과 수평인 경우
        if not x:
            if (y > 0 and d1 == 1 and d2 == 0) or (y < 0 and d1 == 0 and d2 == 1):
                return True

        # x축과 수평인 경우
        else:
            if (x > 0 and d1 == 2 and d2 == 3) or (x < 0 and d1 == 3 and d2 == 2):
                return True

    # 기울기 = 1
    elif m == 1:
        # x1 < x2인 경우
        if x < 0:
            if (d1 == 0 and d2 == 2) or (d1 == 3 and d2 == 1):
                return True
        # x1 > x2인 경우
        else:
            if (d1 == 2 and d2 == 0) or (d1 == 1 and d2 == 3):
                return True

    # 기울기 = -1
    else:
        # x1 < x2인 경우
        if x < 0:
            if (d1 == 1 and d2 == 2) or (d1 == 3 and d2 == 0):
                return True
        # x1 > x2인 경우
        else:
            if (d1 == 2 and d2 == 1) or (d1 == 0 and d2 == 3):
                return True


def collide():
    global ans

    disappear = [0] * N  # 소멸 여부를 확인하고, 값으로 충돌지점과의 거리를 기록

    for distance, i, j in collision:

        if not disappear[i] and not disappear[j]:
            ans += atom[i][3]
            ans += atom[j][3]
            disappear[i] = disappear[j] = distance

        elif disappear[i] == distance and not disappear[j]:
            ans += atom[j][3]
            disappear[j] = distance

        elif disappear[j] == distance and not disappear[i]:
            ans += atom[i][3]
            disappear[i] = distance


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    collision = []
    ans = 0
    if N >= 2:
        candidatates = simulate()   # simulate 함수를 통해 어떤 원자들이 소멸할 수 있는지 후보를 고름
        candidatates.sort()         # 먼저 소멸되는 경우가 있기 때문에 충돌지점과의 거리가 가까운 순으로 정렬시켜서 (그림 속 A와 G는 기울기와 방향만 보면 충돌할 수 있으나, 그 전에 소멸)
        collide()                   # collide 함수를 호출
    print(f'#{tc} {ans}')



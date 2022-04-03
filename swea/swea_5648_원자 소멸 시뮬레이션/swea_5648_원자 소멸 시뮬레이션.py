import sys
sys.stdin = open('sample_input.txt', 'r')

def simulate():
    lst = []
    for i in range(N-1):
        for j in range(i+1, N):
            distance = gradient(atom[i], atom[j])
            if distance:
                lst.append([distance/2, i, j])
    return lst


def gradient(arr1, arr2):
    x = arr1[0] - arr2[0]
    y = arr1[1] - arr2[1]
    if not x:
        if check_diretion(0, x, y, arr1, arr2):
            return abs(y)

    elif not y:
        if check_diretion(0, x, y, arr1, arr2):
            return abs(x)

    elif x / y == 1:
        if check_diretion(1, x, y, arr1, arr2):
            return abs(x)+abs(y)

    elif x / y == -1:
        if check_diretion(-1, x, y, arr1, arr2):
            return abs(x)+abs(y)

    else:
        return


def check_diretion(m, x, y, arr1, arr2):
    d1, d2 = arr1[2], arr2[2]
    if not m:
        if not x:
            if (y > 0 and d1 == 1 and d2 == 0) or (y < 0 and d1 == 0 and d2 == 1):
                return True
        else:
            if (x > 0 and d1 == 2 and d2 == 3) or (x < 0 and d1 == 3 and d2 == 2):
                return True

    elif m == 1:
        if x < 0:
            if (d1 == 0 and d2 == 2) or (d1 == 3 and d2 == 1):
                return True
        else:
            if (d1 == 2 and d2 == 0) or (d1 == 1 and d2 == 3):
                return True

    else:
        if x < 0:
            if (d1 == 1 and d2 == 2) or (d1 == 3 and d2 == 0):
                return True
        else:
            if (d1 == 2 and d2 == 1) or (d1 == 0 and d2 == 3):
                return True


def collide():
    global ans
    added = [0] * N

    for distance, i, j in collision:

        if not added[i] and not added[j]:
            ans += atom[i][3]
            ans += atom[j][3]
            added[i] = added[j] = distance

        elif added[i] == distance and not added[j]:
            ans += atom[j][3]
            added[j] = distance

        elif added[j] == distance and not added[i]:
            ans += atom[i][3]
            added[i] = distance


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    collision = []
    ans = 0
    if N >= 2:
        collision = simulate()
        collision.sort(key=lambda x: x[0])
        collide()
    print(f'#{tc} {ans}')



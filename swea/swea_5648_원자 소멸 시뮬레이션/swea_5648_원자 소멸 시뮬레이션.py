import sys
sys.stdin = open('sample_input.txt', 'r')
import math

T = int(input())


def simulate():
    collision = []
    for i in range(N - 1):
        for j in range(i, N):
            distance = gradient(atom[i], atom[j])
            if distance:
                collision.append([distance/2, i, j])
    return collision


def gradient(arr1, arr2):
    x = arr1[0] - arr2[0]
    y = arr1[1] - arr2[1]

    if not x or not y:
        return check_diretion(0, arr1, arr2)
    elif x / y == 1:
        return check_diretion(1, arr1, arr2)
    elif x / y == -1:
        return check_diretion(-1, arr1, arr2)
    else:
        return


def check_diretion(m, arr1, arr2):
    x1, x2 = arr1[0], arr2[0]
    y1, y2 = arr1[1], arr2[1]
    d1, d2 = arr1[2], arr2[2]
    x, y = x1 - x2, y1 - y2
    flag = False
    if not m:
        if not x:
            if y > 0 and d1 == 0 and d2 == 1 or y < 0 and d1 == 1 and d2 == 0:
                flag = True
        else:
            if x > 0 and d1 == 2 and d2 == 3 or x < 0 and d1 == 3 and d2 == 2:
                flag = True
    elif m == 1:
        if x < 0:
            if d1 == 0 and d2 == 2 or d1 == 3 and d2 == 1:
                flag = True
        else:
            if d1 == 2 and d2 == 0 or d1 == 1 and d2 == 3:
                flag = True
    else:
        if x < 0:
            if d1 == 1 and d2 == 2 or d1 == 3 and d2 == 0:
                flag = True
        else:
            if d1 == 2 and d2 == 1 or d1 == 0 and d2 == 3:
                flag = True
    if flag:
        return math.dist((x1, y1), (x2, y2))


def collide():
    ans = 0
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
    return ans


for tc in range(1, T+1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    collision = simulate()
    collision.sort(key=lambda x: x[0])
    ans = collide()
    print(f'#{tc} {ans}')

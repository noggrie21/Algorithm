from collections import deque


# num번 톱니의 왼쪽편 확인
def check_left(task):
    num, flow = task
    lst = []

    while 1 < num and wheels[num][6] ^ wheels[num-1][2]:
        num -= 1
        flow *= -1
        lst.append((num, flow))

    return lst


# num번 톱니의 오른쪽편 확인
def check_right(task):
    num, flow = task
    lst = []

    while num < 4 and wheels[num][2] ^ wheels[num+1][6]:
        num += 1
        flow *= -1
        lst.append((num, flow))

    return lst


# 작업에 따라 톱니바퀴 돌리기
def work(tasks):
    for num, flow in tasks:
        if flow == 1:
            wheels[num] = clockwise(wheels[num])
        else:
            wheels[num] = c_clockwise(wheels[num])


# 시계방향으로 돌리기
def clockwise(wheel):
    return [wheel[-1]] + wheel[:7]


# 반시계방향으로 돌리기
def c_clockwise(wheel):
    return wheel[1:] + [wheel[0]]


# 톱니의 12시 방향 확인하기
def check(wheels):
    scores = [1, 2, 4, 8]
    result = 0

    for num, score in enumerate(scores, 1):
        if wheels[num][0]:
            result += score

    return result


# 입력
wheels = [[]] + [list(map(int, input())) for _ in range(4)]

N = int(input())

for _ in range(N):
    tasks = [tuple(map(int, input().split()))]

    tasks = tasks + check_left(*tasks) + check_right(*tasks)

    work(tasks)

answer = check(wheels)
print(answer)


boxes = ['apple', 'banana', 'pear']
box = iter(boxes)
print(box)
print(type(box))
print(next(box,'pear'))
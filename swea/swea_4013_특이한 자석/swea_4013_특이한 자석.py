'''
1. T : 테스트 케이스 수
2. K : 자석을 회전시키는 횟수
3. 1번 자석 날 정보
    (N: 0, S: 1)
4. 2번 자석 날 정보
...
6. 4번 자석 날 정보
7. 자석 회전 정보(자석 번호, 회전 방향)
    (1: 시계방향, -1: 반시계방향)

제한 : 하나의 자석이 1칸 회전할 때, 붙어있는 자석은 서로 붙어있는 날의 자석이 다를 경우에만 반대 방향으로 1칸 회전한다
출력 : 모든 자석이 회전이 끝난 후 획득한 점수

아이디어
1. 자석 날이 다른지 같은지 left ^ right = 1일때 -> 움직이기
2. 기준점 index = 0으로 하고, 시계방향으로 회전 +1, 반시계방향으로 회전 -1
3. 필요한 index : 기준점 / 왼쪽 (2, 3, 4번 자석 한정) / 오른쪽 (1, 2, 3번 자석 한정)

'''
from collections import deque
import sys

sys.stdin = open('sample_input.txt')

T = int(input())


def unclock(number):
    magnets[number].append(magnets[number].popleft())
    return


def clock(number):
    magnets[number].appendleft(magnets[number].pop())
    return


for tc in range(1, T+1):
    K = int(input())
    magnets = [deque(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        temp = [0] * 4

        number, direction = map(int, input().split())
        number -= 1
        temp[number] = direction

        left = right = number

        while 0 <= left-1:
            if magnets[left-1][2] ^ magnets[left][6]:
                temp[left-1] = temp[left] * -1
                left -= 1
            else:
                break

        while right+1 < 4:
            if magnets[right+1][6] ^ magnets[right][2]:
                temp[right+1] = temp[right] * -1
                right += 1
            else:
                break

        for i in range(4):
            if temp[i] < 0:
                unclock(i)
            elif temp[i] > 0:
                clock(i)

    answer = 0
    for i in range(4):
        answer += magnets[i][0] * 2 ** i

    print(f'#{tc} {answer}')
import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def DFS(i, total, lst):
    # DFS 종료조건
    if total > num:  # 1. total이 num보다 크면 유효하지 않음으로 함수 종료
        return
    elif total == num:  # 2.total == num이면 lst출력하고 반환값 주기
        print(lst)
        for elem in lst:
            print(elem, end='')
        return 1
    if -i > n:  # 3. num이 가지는 소수개수를 다 돌았으면 함수 종료
        return

    # DFS 다시 호출하기(반환값 존재 시 함수 종료)
    if DFS(i-1, total+2**i, lst+[1]):  # 2**i를 더하는 경우
        return 1
    if DFS(i-1, total, lst+[0]): # 2**i를 더하지 않는 경우
        return 1


for tc in range(1, T + 1):
    num = input()
    n = len(num[2:])  # n: num의 소수부 개수
    num = float(num)

    print(f'#{tc}', end=' ')
    if not DFS(-1, 0, []):  # num은 소수부를 무조건 가지기 때문에 -1부터 시작
        print('overflow', end=' ')
    print()
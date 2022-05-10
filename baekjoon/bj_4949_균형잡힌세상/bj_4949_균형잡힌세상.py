def check(words):
    stack = []   # 괄호들이 담길 배열

    # 입력값 순회돌면서 확인하기(다만, 짝이 안맞는 경우가 발견되면 즉시 함수 종료)
    for char in words:

        # 괄호가 아닌 문자인 경우(그냥 pass)
        if char not in '()[]':
            continue

        # 괄호 문자인 경우
        if char in '([':                    # 여는 괄호,
            stack.append(char)              # (무조건) stack에 추가

        elif stack and ((char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[')):
             stack.pop()                     # stack에서 삭제(닫는 괄호의 짝인 여는 괄호가 삭제됨)

        else:
            print('no')                     # 짝이 안맞으면 'no'출력하고
            return                          # 함수 종료

    # 입력값을 다 확인했을 때
    if not stack:                           # 괄호의 짝이 다 맞은 경우
        print('yes')
    else:                                   # 안맞은 경우
        print('no')
    return


import sys

words = sys.stdin.readline().rstrip()

while words != '.':                         # 입력값이 . 일 경우 순회 종료
    check(words)                            # '.'이 아닌 값일 경우 괄호 검사하기
    words = sys.stdin.readline().rstrip()   # 다음 입력값으로 갱신

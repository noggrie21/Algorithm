import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def check(string):
    temp = []                           # '{('인 경우 항목을 추가 / '})'인 경우 항목 삭제
    idx = -1                            # temp의 인덱스를 가리킬 idx
    for i in range(len(string)):
        if string[i] in '{(':           # 삭제 대상을 temp에 추가하는 과정
            temp.append(string[i])
            idx += 1
        elif string[i] == '}':          # '}'일때 삭제하는 과정
            if temp:                    # 빈리스트가 아닌지 확인
                if temp[idx] == '{':    # 짝 괄호인지 확인
                    temp.pop()          # 짝 괄호면 삭제
                    idx -= 1
                else:
                    break
            else:
                break
        elif string[i] == ')':          # ')'일때 삭제하는 과정
            if temp:                    # 빈리스트가 아닌지 확인
                if temp[idx] == '(':    # 짝 괄호인지 확인
                    temp.pop()          # 짝 괄호면 삭제
                    idx -= 1
                else:
                    break
            else:
                break
    else:                               # 위의 for문을 다 돌고
        if not temp:                    # temp가 다 비었을때에만
            return 1                    # retrun 1을 받을 수 있음


for tc in range(1, T+1):
    s = input()
    if not check(s):
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {1}')





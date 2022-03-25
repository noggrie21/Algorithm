import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def cnt(str1, str2, a, b):       # 반복 횟수를 구하는 함수(중복 없이)
    result = 0
    i = 0
    while i < a:                 # 비교대상(str1)의 유효한 인덱스 범위에서만
        if str1[i:i+b] == str2:  # 반복(a+b-1)로하면 불필요한 작업이 추가되는 거지 인덱스 에러가 나는 건 아님
            result += 1          # 상은님 코드....
            i += b               # 일치하는 인덱스의 다음 인덱스부터 확인할 수 있도록
        else:
            i += 1               # 일치하지 않을 때에는 순차적으로 확인할 수 있도록
    return result

    # 실패사례.. xxxxxx xx일 때 오류...
    # for i in range(a - b + 1):
    #     if str1[i:i+b] == str2:
    #         result += 1
    # return result


for tc in range(1, T+1):
    A, B = map(str, input().split()) # A = banana / B = bana
    a, b = len(A), len(B) # a = A의 길이 / b = B의 길이
    typing = a - (b - 1) * cnt(A, B, a, b) # 타이핑 횟수 = 전체 길이 - (반복되는 단어의 길이 - 1) * 반복 횟수
    print(f'#{tc} {typing}')

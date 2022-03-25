import sys
sys.stdin = open('input (1).txt')

# 스택구조로 풀기
for tc in range(1, 11):
    N, s = input().split()
    result = '!'                    # result를 인덱스에러 방지 임의 글자 넣기
    while s:
        if s[-1] != result[-1]:     # 같지 않으면 삽입
            result += s[-1]         # 넣을 때는 s를 뒤집은 형태로
        else:                       # 같으면 result 맨 앞 값 제거
            result = result[:-1]
        s = s[:-1]
    print(f'#{tc} {result[:0:-1]}')

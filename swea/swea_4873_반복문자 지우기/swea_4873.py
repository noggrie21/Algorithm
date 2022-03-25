import sys
sys.stdin = open('sample_input.txt')

# 문자열 s에서 맨 앞 값을 하나씩 뺀다.
# 만일, result의 맨 앞 값과 다르면 넣고,
# 같으면 넣지 않고 그리고 result의 맨 앞 값도 제거한다.
# s를 앞에서부터 하나씩 줄여나가며 반복한다.


T = int(input())


for tc in range(1, T+1):
    s = input()
    result = '!'                    # result를 인덱스로 접근하기 때문에 임의의 글자
    while s:
        if s[0] != result[0]:       # 같지 않으면 삽입
            result = s[0] + result  # 넣을 때는 s를 뒤집은 형태로
        else:                       # 같으면 result 맨 앞 값 제거
            result = result[1:]
        s = s[1:]
    print(f'#{tc} {len(result)-1}')














# for tc in range(1, T+1):
#     s = input()
#     result = '!'                    # result를 인덱스로 접근하기 때문에 임의의 글자
#     while s:
#         temp = s[0]
#         if temp != result[0]:
#             result = temp + result
#         else:
#             result = result[1:]
#         s = s[1:]
#     print(f'#{tc} {len(result)-1}')
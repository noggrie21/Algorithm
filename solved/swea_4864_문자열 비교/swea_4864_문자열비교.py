import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    pattern = input()
    text = input()
    p_len = len(pattern)
    t_len = len(text)
    result = 0

    for i in range(t_len-p_len+1):
        for j in range(p_len): # 상은님꺼 코드 확인해보기(밑에)
            if text[i+j] != pattern[j]:
                break
        else:
            result += 1
            break
    print(f'#{tc} {result}')


# 상은님 코드
# if text[i:i+p_len] == pattern:
#     result = 1
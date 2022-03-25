import sys
sys.stdin = open('input (1).txt')

for tc in range(1, 11):
    N, s = input().split()
    stack = []

    # 첫번째 풀이
    # for i in range(int(N)):
    #     if not stack:
    #         stack.append(s[i])
    #     else:
    #         if stack[-1] == s[i]:
    #             stack.pop()
    #         else:
    #             stack.append(s[i])

    # 첫번째 풀이에서 stack.append(s[i])가 중복되니 이걸 하나로 합치기
    for i in range(int(N)):
        if not stack and stack[-1] != s[i]:
            stack.append(s[i])
        else:
             stack.pop()
    print(f'#{tc}', ''.join(stack))
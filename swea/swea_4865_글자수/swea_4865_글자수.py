import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())

for tc in range(1, T+1):     # str1의 각 문자가 str2에서 몇 번 반복되냐를 찾는 거여서
    str1 = set(input())      # set()을 통해 중복 제거 tc = 2일때, str1 = {'S', 'T', 'J'}
    str2 = input()
    max_cnt = 0

    for i in str1:           # str1을 순회하면서 i : 'S'>'T'>'J'
        cnt = 0
        for j in str2:       # j : 'H'>'O'>'F'>'S'>'T'>'J'>'P'>'V'>'P'>'P'
            if i == j:       # str2와 같으면
                cnt += 1
        if max_cnt < cnt:    # cnt가 더 큰 경우 max_cnt 갱신
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')

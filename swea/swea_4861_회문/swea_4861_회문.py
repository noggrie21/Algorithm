import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def s_e(arr):                              # s_e() : 회문 판독기
    test = arr[:]                          # 인덱스 슬라이싱을 이용해서 확인하기 때문에,
    while len(test) > 1:                     # test를 생성(원본에서 값 복사한 리스트)
        if test[0] == test[-1]:              # 첫번째 글자와 마지막 글자가 같으면
            test = test[1:-1]                # 두번째 글자와 마지막 바로 앞 글자까지 test에 재할당
        else:
            break
    if len(test) <= 1:
        return ''.join(arr)

# A = ['G', 'b', 'c', 'd']
# B = ['a', 'b', 'b', 'a']
# C = ['a', 'b','c' ,'b', 'a']


for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    # result = ['JAEZNNZEAJ',None]

    # 행 탐색
    for i in range(N):
        for j in range(N-M+1):
            temp = []
            for k in range(M):
                temp.append(board[i][j+k])
            result.append(s_e(temp))

    # 열 탐색
    for i in range(N):
        for j in range(N-M+1):
            temp = []
            for k in range(M):
                temp.append(board[j+k][i])
            result.append(s_e(temp))

    result = list(filter(None, result))
    print(f'#{tc}', ' '.join(result))     # result = ['JAEZNNZEAJ','aba']

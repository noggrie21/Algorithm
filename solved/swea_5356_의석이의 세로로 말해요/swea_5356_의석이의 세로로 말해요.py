import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    text = [[0]*15 for _ in range(5)]
    board = [list(input()) for _ in range(5)]
    print(board)
    for i in range(5):
        for j in range(15):
            try:
                text[i][j] = board[i][j]
            except:
                text[i][j] = 0


    # 여기 더 생각해보고 싶어용.. 뭔가 줄일 수 있을 거 같은?
    result = []
    for i in range(15):
        for j in range(5):
            result.append(text[j][i])
    print(f'#{tc}', ''.join(filter(None, result)))

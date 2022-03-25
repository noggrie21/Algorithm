import sys
sys.stdin = open('input.txt')

# 행방향 탐색
def cnt_palindrome(arr):
    max_cnt = 1
    for i in range(100):
        for j in range(100):
            # temp = []
            for k in range(j + 1, 100):
                if arr[i][j] == arr[i][k]:
                    # temp = matrix[i][j:k+1]
                    cnt = cnt_palindrome(arr[i][j:k + 1])
                    if max_cnt < cnt:
                        max_cnt = cnt
    return max_cnt


for _ in range(1):
    tc = int(input())
    matrix = [list(input()) for _ in range(100)]
    print(cnt_palindrome(matrix))
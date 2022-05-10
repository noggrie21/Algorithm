T = int(input())
for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    if N % H:
        print(f'{N%H}{N//H+1:02}')
    else:
        print(f'{H}{N//H:02}')
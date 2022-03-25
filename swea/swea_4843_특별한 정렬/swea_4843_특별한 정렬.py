import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    new_arr = [0] * 10 # 출력할 결과를 담기 위한 리스트 생성

    for i in range(N-1, 0, -1): # 버블 정렬로 arr 오름차순 만들기
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    for i in range(0, 10, 2):       # new_arr에 값 추가를 위한 순회
        new_arr[i] = arr[-1]        # arr의 가장 큰 값을 new_arr[i]에
        new_arr[i+1] = arr[0]       # arr의 가장 작은 값을 new_arr[i+1]에
        arr = arr[1:-1]             # arr 갱신(new_arr에 넣은 값 제외시키기)
    print(f'#{tc}', *new_arr)


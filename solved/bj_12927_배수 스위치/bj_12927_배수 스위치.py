def trans(arr):
    for i in range(1, N):
        if arr[i] == 'Y':
            arr[i] = 1
        else:
            arr[i] = 0
    return arr


lights = [0] + list(input())
N = len(lights)
trans(lights)                    # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1] 맨 앞 가짜값
cnt = 0
for i in range(1, N):        # 켜져있는 스위치 번호 찾기
    if lights[i]:
        for j in range(i, N, i):  # 켜져있는 번호와 그 배수의 번호 스위치 전환하기
            lights[j] = lights[j] ^ 1
        cnt += 1
if sum(lights) != 0:
    cnt = -1
print(cnt)

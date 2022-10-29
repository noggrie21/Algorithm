'''
누적합을 이용
lamp[1]부터 lamp[K]까지 [정상 갯수, 고장 갯수]로 초기화된 배열에
옆으로 한칸씩 움직이면서 상태 갯수값 조정해주기

1. lamp 배열 만들기 lamp[num]: num번의 상태(1은 정상, 0은 고장)
2. 초기화된 상태 배열 만들기: status의 길이는 K
3. 2부터 돌면서 N-4까지 앞에 신호등 상태 빼주고 뒤 신호등 상태 더해주기
   이때 제일 작은 경우의 수 체크해주기

'''

N, K, B = map(int, input().split())

# 1
lamp = [0] + [1] * N
for _ in range(B):
    lamp[int(input())] = 0

# 2
status = [0, 0]
for k in range(1, K+1):
    status[lamp[k]] += 1

# 3
answer = status[0]
for i in range(2, N-K+2):
    status[lamp[i-1]] -= 1
    status[lamp[i+K-1]] += 1

    if status[0] < answer:
        answer = status[0]

print(answer)


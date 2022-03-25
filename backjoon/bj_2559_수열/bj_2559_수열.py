# 수업시간에 봤던 윤혁님 코드 참고

N, K = map(int, input().split())
weather = list(map(int, input().split()))

max_result = 0                  # 기온이 음수인 경우도 가능하기 때문에 K일 동안 온도의 합으로 초기값 설정
for i in range(K):
    max_result += weather[i]

result = max_result

for i in range(1, N-K+1):       # 초기값으로 이미 계산했기 때문에 1부터 시작
    result -= weather[i-1]      # 이미 구해진 k일 온도의 합에서 전날의 온도를 빼고
    result += weather[i+K-1]    # 새롭게 추가된 날의 온도를 더함
    if max_result < result:
        max_result = result
print(max_result)
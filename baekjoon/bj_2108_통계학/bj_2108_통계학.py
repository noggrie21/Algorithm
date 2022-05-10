def mode(numbers):
    maxC = cnt = 0                      # maxC: cnt 최댓값 / cnt: 출연 횟수(같은 숫자가 한 번 나올때부터 cnt가 +1 됨)
    i = 0                               # i: numbers 인덱스(기준 숫자를 가리킴)
    j = i+1                             # j: numbers 인덱스(비교 숫자를 가리킴)
    cnt_index = []                      # (해당 숫자 출연 횟수, 해당 숫자의 인덱스) 요소가 담긴 배열
    numbers += [numbers[0]]             # numbers의 마지막 숫자까지 순회하기 위해 더미 요소 추가하기

    while i < N and j <= N:
        if numbers[i] == numbers[j]:    # 기준(numbers[i])와 비교대상(numbers[j])이 같으면,
            j += 1                      # 다른 비교대상으로 교체
            cnt += 1                    # 기준 숫자의 출연 횟수 +1
        else:
            cnt_index.append((cnt, i))  # 다르면,
            i = j                       # 비교대상의 위치로 기준 숫자를 갱신
            j = i+1                     # 기준이 바뀌었기 때문에, 그에 따라 비교대상도 갱신
            maxC = max(maxC, cnt)       # 지금까지 구한 cnt가 maxC보다 크면 갱신
            cnt = 0                     # cnt 초기화

    cnt_index = list(filter(lambda x: x if x[0] == maxC else False, cnt_index))

    if not cnt_index:
        return numbers[0]
    elif cnt_index[0] == cnt_index[-1]:
        return numbers[cnt_index[0][1]]
    else:
        return numbers[cnt_index[1][1]]


import sys
N = int(input())
numbers = []
total = 0

for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    total += number
    numbers.append(number)

numbers.sort()
ans1 = round(total/N)                   # 산술평균
ans2 = numbers[N//2]                    # 중앙값
ans4 = abs(numbers[-1]-numbers[0])      # 범위
ans3 = mode(numbers)                    # 최빈값

print(ans1)
print(ans2)
print(ans3)
print(ans4)

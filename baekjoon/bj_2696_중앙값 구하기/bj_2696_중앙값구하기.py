T = int(input())                                # T: 테스트 케이스 갯수

for _ in range(T):
    N = int(input())                            # N: 수열의 크기

    cnt = N//2+1                                # cnt: 출력하는 중앙값 갯수

    lst = []                                    # lst: 전체 수열이 담긴 배열
    answer = []                                 # answer: 출력하는 중앙값이 담긴 배열

    for n in range(N//10+1):
        # ex) 원소가 9개 -> 1줄 입력 받아야 함 / 원소가 23개 -> 3줄 입력 받아야 함
        # 즉, N//10+1번 순회해야 함

        line = list(map(int, input().split()))  # line: 10개씩 나눈 부분 수열

        for th in range(len(line)):

            lst.append(line[th])

            if not th % 2:
                lst.sort()
                answer.append(lst[(th+n*10)//2])

    # 출력
    print(cnt)

    for i in range(cnt//10+1):
        print(*answer[10*i:10*i+10])



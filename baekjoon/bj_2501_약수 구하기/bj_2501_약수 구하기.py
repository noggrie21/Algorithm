N, K = map(int, input().split())
k = answer = 0

for i in range(1, N+1):

    # i가 N의 약수일 떄,
    if not N % i:
        k += 1

        # K번째 약수면
        if k == K:
            answer = i
            break

print(answer)
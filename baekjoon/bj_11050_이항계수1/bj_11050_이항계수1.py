def combination(N, K):
    M = N - K

    if K > M:
        K, M = M, K

    denominator = numerator = 1
    # 분모 = 분자 = 1

    for k in range(K, 0, -1):
        numerator *= N
        N -= 1
        denominator *= k

    print(numerator // denominator)


N, K = map(int, input().split())
combination(N, K)

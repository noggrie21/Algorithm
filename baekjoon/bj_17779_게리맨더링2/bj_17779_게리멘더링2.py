def simulate_standard():
    minV = 100 * 20

    for r in range(1, N-1):
        for c in range(N-2):
            value = simulate_delta(r, c)
            minV = min(value, minV)

    return minV


def simulate_delta(r, c):

    minV = 100 * 20
    for d1 in range(1, N-r):
        for d2 in range(1, N-c):
            if 0 <= r - d1 and r - d1 + d2 <= N and 0 <= c + d1 + d2 < N:
                big, small = count_population(r, c, d1, d2)
                minV = min(big-small, minV)

    return minV


def count_population(r, c, d1, d2):
    print(r, c, d1, d2)
    population = [0] * 5

    for i in range(N):
        for j in range(N):

            if r - d1 <= i <= r + d1 and c <= j <= c + d1 + d2:
                if r == 6 and c == 5:
                    print(i, j)
                population[4] += city[i][j]

            elif 0 <= i < r and 0 <= j < c + d1:
                population[0] += city[i][j]

            # 2번 선거구
            elif 0 <= i < r + d2 and c + d1 <= j < N:
                population[1] += city[i][j]

            # 3번 선거구
            elif r <= i < N and 0 <= j < c - d1 + d2:
                population[2] += city[i][j]

            # 4번 선거구
            elif r + d2 <= i < N and c - d1 + d2 <= j < N:
                population[3] += city[i][j]


    print(population)
    return max(population), min(population)


N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
print(simulate_standard())
# print(city)
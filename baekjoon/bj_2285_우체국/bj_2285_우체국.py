N = int(input())

village = [tuple(map(int, input().split())) for _ in range(N)]
# print(village)
answer = -1
min_diff = 1000000000 * N

for destination in village:
    postoffice, dum = destination
    diff = 0

    for near in village:
        house, people = near
        diff += abs(postoffice - house) * people
    # print(diff, postoffice, min_diff)
    if diff < min_diff or (diff == min_diff and postoffice < answer):
        min_diff = diff
        answer = postoffice

print(answer)

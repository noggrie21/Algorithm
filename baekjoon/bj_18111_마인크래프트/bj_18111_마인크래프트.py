def onlydump(length,lst):
    i = time = 0
    j = 1

    while j < length:
        if lst[i] != lst[j]:
            time += (2*(lst[j]-lst[i]))
        j += 1

    return time, lst[i]


def dump_fill(length, inven, lst):
    high = time = 0
    return time, high

    


N, M, B = map(int, input(). split())
lst = []
for _ in range(N):
    lst.extend(list(map(int, input().split())))

lst.sort()

# 제일 낮은 땅 기준으로 파내기만 실행
ans1 = onlydump(N*M, lst[:])


# 파내고 메꾸고 같이 실행
ans2 = dump_fill(N*M, B, lst[:])


# 최소 시간 작업에 대한 높이 출력(소요 시간 동일 시 더 높은 경우 출력)
if ans1[0] < ans2[0]:
    print(ans1)
elif ans1[0] == ans2[0]:
    print(ans1[0], max(ans1[1], ans2[1]))
else:
    print(ans2)
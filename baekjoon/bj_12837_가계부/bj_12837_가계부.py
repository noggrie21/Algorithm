N, Q = map(int, input().split())

note = [0]*(N+1)  # 생후 xx일에 대한 정보를 note[xx]에 담을 수 있도록 리스트 생성
old = 0  #
big = 0
total = 0
for _ in range(Q):
    n, p, v = map(int, input().split())

    # 기록할 때
    if n == 1:
        total += v

        if p >= old:
            note[p] += v
            while old+1 != p:
                note[old+1] += note[]


            old = p

        else:


    # 출력할 때
    else:


# for i in range(1, N+1):
#     note[i] = note[i-1] + note[i]
# for b, a in d:
#     print(abs(note[b]-note[a]))
# # print(note)
# # print(d)
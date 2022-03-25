def solution(id_list, report, k):
    N = len(id_list)
    answer = [0] * N
    blacklist = {}  # {신고당한 유저 : [신고한 유저1, 신고한 유저2], 신고당한 유저2 : [신고한 유저1, 신고자2] }
    for users in report:  # report를 통해 blacklist 완성시키기
        ing, ed = users.split()
        if not blacklist.get(ed):
            blacklist[ed] = [ing]
        else:
            if ing not in blacklist[ed]:
                blacklist[ed] += [ing]
    print(blacklist)

    mail = {}   # {신고한 유저 id: cnt}메일 발송받을 사람 추리기
    for ings in blacklist.values():
        print(ings)
        if k <= len(ings):
            for ing in ings:
                if ing in mail:
                    mail[ing] += 1
                else:
                    mail[ing] = 1
    print(mail)

    for i in range(N):
        if not mail.get(id_list[i]):
            answer[i] = 0
        else:
            answer[i] = mail.get(id_list[i])
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
solution(id_list, report, k)
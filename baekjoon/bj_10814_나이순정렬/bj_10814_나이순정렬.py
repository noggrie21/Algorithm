def switch(char):
    if char.isdecimal():
        char = int(char)
    return char


N = int(input())
users = [[i] + list(map(switch, input().split())) for i in range(N)]

# 회원 나이가 증가하는 순, 나이가 같으면 먼저 가입한 사람이 앞에오는 순
users.sort(key=lambda x:(x[1], x[0]))

for user in users:
    print(user[1], user[2])

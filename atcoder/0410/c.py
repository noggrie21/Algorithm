N = int(input())

s = [1]

if N == 1:
    print(*s)
else:
    for n in range(2, N+1):
        s = s + [n] + s
    print('10번째', *s)


S = '1'

if N == 1:
    print(S)
else:
    for n in range(2, N+1):
        S = S + f'{n}' + S
    print('20번째', ' '.join(S))
print(s)
print(list(map(int, S)))
if s == list(map(int, S)):
    print('Yes')
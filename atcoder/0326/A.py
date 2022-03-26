a, b, c, d = map(int, input().split())
T = (a, b)
A = (c, d)

result = 'Takahashi'

if T[0] > A[0]:
    result = 'Aoki'
elif T[0] == A[0] and T[1] > A[1]:
    result = 'Aoki'

print(result)
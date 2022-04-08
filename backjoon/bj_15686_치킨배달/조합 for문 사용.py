def fixed(N, R):
    for i in range(N-R+1):
        for j in range(i+1, N-R+2):
            for k in range(j+1, N):
                print([arr[i], arr[j], arr[k]])

arr = [6, 7, 8, 9, 10]
fixed(5, 3)

a = [1, 2, 3]
b = ['가', '나', '다']
# print(list(zip(*reversed(b))))
print(list(reversed(b)))
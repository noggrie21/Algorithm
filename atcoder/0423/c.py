N, K = map(int, input().split())
alphabets = [0] * 26
for i in range(1, N+1):
    temp = [0] * 26
    for alphabet in input():
        idx = ord(alphabet) - ord('a')
        # print(ord(alphabet))
        if temp[idx]:
            alphabets[ord(alphabet) - ord('a')] = N+1
        else:
            temp[idx] += 1
            alphabets[ord(alphabet) - ord('a')] += 1
    print('temp', temp)

ans = 0
print(alphabets)
for alphabet in alphabets:
    if K <= alphabet <= N:
        ans += 1
print(ans)
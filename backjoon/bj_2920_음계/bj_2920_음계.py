pitches = [list(range(1, 9)), list(range(8, 0, -1))]
ans = ['ascending', 'descending']
pitch = list(map(int, input().split()))

for i in range(2):
    if pitches[i] == pitch:
        print(ans[i])
        break
else:
    print('mixed')

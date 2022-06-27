first = []
last = []
N = int(input())
result = 'No'

for _ in range(N):
    f, l = input().split()
    first.append(f)
    last.append(l)

# print(first, last)

if (len(set(first)) == N or len(set(last)) == N) and not set(first).intersection(set(last)):
    result = 'Yes'
    print(result)
elif first.index(set(first).intersection(set(last))) == last.index(set(first).intersection(set(last))):
    result = 'Yes'
    print(result)
else:
    print(result)


# for i in range(N):
#     for j in range(N):
#         if i != j:
#             if first[i] != first[j] and first[i] != last[j]:
#
# #     if first[i] not in last[:i+1] and first[i] not in last[i+1:] and not in :
# #         continue
# #     elif last[i] not in first[:i+1] and last[i] not in first[i+1:]:
# #         continue
# #     else:
# #         print('No')
# #         break
# # else:
# #     print('Yes')


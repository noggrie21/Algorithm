def make_serizes(original):
    result = []
    for num in original:
        for i in '123456789':
            result.append(i+num)
        for j in '0123456789':
            result.append(num+j)
    return result


N = int(input())

# 자릿 수 계산을 위한 리스트 n만들기
n = [1] + [0] * 4
for i in range(1, 5):
    n[i] = n[i-1] + 19**i

# 자릿 수 계산하기
i = 0
while N > n[i]:
    i += 1
digit = i + 3
print(digit)
lst = ['666']
for cnt in range(3, digit):
    lst += make_serizes(lst)

lst = list(map(int, set(lst)))
lst.sort()
print(lst)
print(lst[N-1])



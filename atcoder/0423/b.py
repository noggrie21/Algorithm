S = input()
n = len(S)
result = "No"
s = set(S)

if len(s) == n:
    check_upper = 0
    check_lower = 0
    for char in s:
        if char.isupper():
            check_upper = 1
        else:
            check_lower = 1
    if check_upper + check_lower == 2:
        result = "Yes"

print(result)

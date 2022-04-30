N = int(input())

for _ in range(N):
    stack = 0
    string = input()
    for char in string:
        if char == '(':
            stack += 1
        else:
            if not stack:
                break
            stack -= 1
    else:
        if not stack:
            print('YES')
            continue
    print('NO')
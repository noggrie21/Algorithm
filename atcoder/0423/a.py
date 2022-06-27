'''
A B C D E F X
'''


def walk(limit, speed, runtime, breaktime, total, status):
    if limit <= 0:
        return total
    else:
        # 뛸 때,
        if status:
            temp = limit - runtime
            if 0 <= temp:
                ans = walk(temp, speed, runtime, breaktime, total + speed * runtime, 0)
            else:
                ans = walk(temp, speed, runtime, breaktime, total + speed * (runtime + temp), 0)
        # 쉴 때,
        else:
            temp = limit - breaktime
            ans = walk(temp, speed, runtime, breaktime, total, 1)

        if ans:
            return ans


T_run, T_speed, T_break, A_run, A_speed, A_break, X = map(int, input().split())

tsum = walk(X, T_speed, T_run, T_break,  0, 1)
asum = walk(X, A_speed, A_run, A_break, 0, 1)
result = "Draw"

if tsum < asum:
    result = "Aoki"
elif tsum > asum:
    result = "Takahashi"
print(result)

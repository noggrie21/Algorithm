'''
현재 한수의 위치(x, y)

출력 : 직사각형의 경계선까지 가는 거리의 최솟값

1 ≤ w, h ≤ 1,000
1 ≤ x ≤ w-1
1 ≤ y ≤ h-1
x, y, w, h는 정수
'''

x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))



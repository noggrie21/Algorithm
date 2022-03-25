def find(area):
    max_ruin = 0
    for line in area:
        for ruin in line.split('0'):
            now = len(ruin)
            if now > 1 and now > max_ruin:
                max_ruin = now
    return max_ruin

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    area = [input().replace(' ', '') for _ in range(n)]
    width = find(area)
    vertical = [''.join(line) for line in list(zip(*area))]
    height = find(vertical)
    result = max(width, height)
    print('#{0} {1}'.format(tc, result))
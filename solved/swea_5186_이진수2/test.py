import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def recur(i, end,s,number): # 13개의 수가 각각 포함될 때 또는 포함되지 않을 떄 완성할 수 있는지
    global temp
    if i == end:
        if sum(s) == number:
            temp = s
            return
    else:
        recur(i+1, end, s + [value[i]], number) # 포함될 떄
        recur(i+1, end, s + [0], number) # 포함되지 않을 떄

value = [2**i for i in range(-1,-14,-1)]

for tc in range(T):
    number = float(input())
    temp =[]
    recur(0,13,[],number)
    if sum(temp) == 0:
        print(f'#{tc+1} overflow') # 포함되지 않으면 temp에 담긴 수가 없음
    else:
        for i in range(len(temp)-1,-1,-1): # 뒤에서부터 0이 아닌 수가 나온 위치를 찾고 맨 앞부터 해당 위치까지 중에 0이면 0, 0이 아니면 1로 변환
            if temp[i]!=0:
                print(f"#{tc+1} {''.join(list(map(lambda n:'1' if n !=0 else '0',temp[0:i+1])))}")
                break



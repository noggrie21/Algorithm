import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def play(arr): # babygin인지 확인하는 함수(가지고 있는 카드가 점수를 획득 할 수 있는 지 확인)
    score = 0

    counts = [0] * 10                                               # 주어진 arr의 카운트 배열 만들기
    for i in arr:
        counts[i] += 1

    i = 0
    while i < 10:
        if i <= 7 and counts[i] and counts[i+1] and counts[i+2]:    # 연속적인 숫자카드나
            score += 1                                              # 점수 획득
            break
        if counts[i] >= 3:                                          # 같은 숫자가 3장 이상이면
            score += 1                                              # 점수 획득
            break
        i += 1

    return score


def match(player1, player2, cards):
    for i in range(len(cards)):                                     # 남은 숫자카드를 의미하는 cards 순회하며

        if not i % 2:                                               # 홀수번째 나오는 카드는
            player1.append(cards[i])                                # player1에게 주고
            if play(player1):                                       # 점수를 획득할 수 있는 카드 셋인지 확인
               return 1                                             # 점수가 있으면, player1의 승리를 의미하는 1 반환

        else:                                                       # 짝수번째 나오는 카드는
            player2.append(cards[i])                                # player2에게 주고
            if play(player2):                                       # 점수를 획득할 수 있는 카드셋인지 확인
                return 2                                            # 점수가 있으면, player2의 승리를 의미하는 2 반환

    return 0                                                        # 모든 차례가 끝나고도 아무도 획득 점수가 없으면 무승부를 의미하는 0 반환


for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    # 승부를 확인하지 못하는 최대한의 카드 갯수로 세팅하기
    player1 = cards[0:4:2]
    player2 = cards[1:4:2]

    # 6장을 뺀 나머지 숫자 카드로 갱신
    cards = cards[4:]

    print(f'#{tc} {match(player1, player2, cards)}')



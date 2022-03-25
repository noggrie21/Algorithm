import sys
sys.stdin = open('input (1).txt', 'r')

T = int(input())

number = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


def search(array, N, M):
    '''
    첫 for문에서 array의 요소를 하나씩 꺼내고,
    만약 해당 요소에 '1'이 포함되어 있을 경우에
    다음 for문 순회시작 (j는 뒤에서부터 순회)
    '1'을 만나면 해당 암호가 정상 코드인지 확인하는 certify함수를 호출하면서 해당 함수는 종료
    '''
    for i in range(N):
        if '1' in array[i]:
            for j in range(M-1, -1, -1):
                if array[i][j] == '1':
                    return certify(array[i][j-55:j+1])


def certify(code):
    '''
    odd : 홀수 자리의 합이 담길 변수 / even : 전체의 합이 담길 변수
    암호코드는 8개의 숫자이기 때문에 8번 순회하며, 7개씩 (인덱스 슬라이싱을 이용하여) 끊어서
    일치하는 숫자 value에 담기
    홀수 자리일때에는 odd에 합산 / 짝수 자리(검증코드 포함)일때에는 even에 합산
    odd*3 + even이 유효한 코드면 return odd + even / 유효하지 않으면 return 0
    '''
    odd = 0
    even = 0

    for i in range(8):
        value = number[code[i * 7:(i * 7) + 7]]
        if i % 2:
            even += value
        else:
            odd += value

    if not (odd * 3 + even) % 10:
        return odd + even

    return 0


for tc in range(1, T + 1):
    N, M = map(int, input().split())      # N: 세로, M: 가로
    array = [input() for _ in range(N)]   # array = ['000', '001, '000'] 이런식으로 입력 받기
    ans = search(array, N, M)
    print(f'#{tc} {ans}')

import sys
sys.stdin = open('GNS_test_input.txt')
# sys.stdin = open('GNS_output.txt', w) - 파일로 출력받기

T = int(input())
num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    x = input().split()
    N = int(x[1])
    num = input().split()
    counts_dict = {}                           # {'ZRO':갯수, 'ONE':갯수,...} 쌍으로 이루어진 딕셔너리 만들기

    for i in range(N):                         # counts_dict 딕셔너리 채우기
        try:
            counts_dict[num[i]]
        except KeyError:
            counts_dict[num[i]] = 0
        finally:
            counts_dict[num[i]] += 1

    result = []                                # 반환할 리스트
    # for j in range(10):                        # num_list을 순회하며
    #     while counts_dict[num_list[j]] > 0:    # counts_dict[num_list[0]] : 'ZRO'의 갯수(갯수가 0이 될때까지 반복)
    #         result += [num_list[j]]            # [num_list[0]] : 'ZRO'
    #         counts_dict[num_list[j]] -= 1      # 'ZRO'의 갯수 하나씩 감소

    for i in num_list:
        for j in range(counts_dict[i]):
            print(i, end=" ")
    print()


    for j in num_list:
        result.append(counts_dict[j] * (j+' '))
        # print(result)
    result = ''.join(result)
    # print(result)
    print(f'#{tc}')
    print(result)


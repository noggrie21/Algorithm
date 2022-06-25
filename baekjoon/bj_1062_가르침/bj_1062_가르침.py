from copy import deepcopy

def filtering(words, chars):
    result = []
    for word in words:
        word = set(filter(lambda x: False if x in chars else True, word))
        result.append(word)
        # result.append(''.join(word))
    return result


def nCr(r, start, last, removals):
    global answer
    global words

    # 기저 파트
    if not r:
        print(removals)
        # print(words)
        temp = word
        words = filtering(words, removals)
        answer = max(answer, N-len(words))
        return

    # 유도 파트
    for idx in range(start, last):
        nCr(r-1, idx+1, last, removals + [alphabets[idx]])


# 입력
N, K = map(int, input().split())
answer = 0

words = list(set(input()) for _ in range(N))

if K >= 5:
    words = filtering(words, 'antic')
    print('words', words)

    alphabets = set()
    for word in words:
        print(word)
        alphabets = alphabets.union(word)
    alphabets = ''.join(alphabets)
    print('alphabets', alphabets)

    nCr(K-5, 0, len(alphabets), [])

# 출력
print(answer)
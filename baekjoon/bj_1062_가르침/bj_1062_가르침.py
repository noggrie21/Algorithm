# from copy import deepcopy
#
# def filtering(words, chars):
#     result = []
#     for word in words:
#         word = set(filter(lambda x: False if x in chars else True, word))
#         result.append(word)
#         # result.append(''.join(word))
#     return result
#
#
# def nCr(r, start, last, removals):
#     global answer
#     global words
#
#     # 기저 파트
#     if not r:
#         # print('removals', removals)
#         # print(words)
#         temp = deepcopy(words)
#         temp = filtering(temp, removals)
#         # print(temp)
#         # print(list(filter(None, temp)))
#         answer = max(answer, N-len(list(filter(None, temp))))
#         return
#
#     # 유도 파트
#     for idx in range(start, last):
#         nCr(r-1, idx+1, last, removals + [alphabets[idx]])
#
#
# # 입력
# N, K = map(int, input().split())
# answer = 0
#
# words = list(set(input()) for _ in range(N))
#
# if K >= 5:
#     words = filtering(words, 'antic')
#     # print('words', words)
#
#     alphabets = set()
#     for word in words:
#         # print(word)
#         alphabets = alphabets.union(word)
#     alphabets = ''.join(alphabets)
#     # print('alphabets', alphabets)
#
#     nCr(K-5, 0, len(alphabets), [])
#
# # 출력
# print(answer)
#

'''
목표 : 학색들이 되도록 많은 단어를 읽게 만들기
제한(규칙)
1. (지민) K개의 글자를 가르칠 시간밖에 없음
2. (학생) K개의 글자로만 이루어진 단어만 읽을 수 있음
3. 남극언어의 단어는 N개밖에 없고, 모든 단어는 anta로 시작, tica로 끝남

출력 : K개의 글자를 가르칠 때 학생들이 읽을 수 있는 단어 개수 최댓값

N, K: 단어 개수 (0 < N <= 50, 0 <= K <= 26)
N개의 남극 단어 (8 <= 남극 단어의 길이 <= 15)


일단 K가 5 이상이어야 함(남극 단어는 무조건 anta, tica를 포함하기 때문에)
1. K가 5 이상인지 확인 -> 아니면 바로 print(0)
2. 단어에서 하나씩 입력을 받을 건데 여기서 antic를 없애고 받기
3.
'''


def my_filter(N):
    alphabet = [0] * 26
    words = list(set(input()) for _ in range(N))
    filtered_words = set()

    for word in words:
        for char in word:
            if char not in 'antic':
                alphabet[ord(char)-ord('a')] += 1
                filtered_words.add(char)

    letter = list(zip(list(range(26)), alphabet))
    return letter, filtered_words, words, alphabet


def nCr(r, start, selected):
    global answer
    # 종료 파트
    if r <= 0:
        cnt = 0
        print('최종 선택', selected)
        for word in filtered_words:
            print('word', word)
            for char in word:
                print(word, char, selected)
                if ord(char) not in selected:
                    break
        else:
            cnt += 1
            print('통과', cnt, word, selected)
        answer = max(cnt, answer)
        return

    # 유도 파트
    for i in range(start, len(letter)):
        if not used[i]:
            used[i] = 1
            nCr(r-1, i, selected+[letter[i][0]])
            used[i] = 0


N, K = map(int, input().split())
answer = 0

if K < 5:
    print(0)

elif K == 26:
    print(N)

else:
    letter, filtered_words, words, alphabet = my_filter(N)
    letter = list(filter(lambda x:True if x[1] else False, letter))
    print(letter)
    letter.sort(key=lambda x:-x[1])
    print('letter',letter )
    print('filtered_words', filtered_words)
    print('alphabet', alphabet)
    used = [0] * len(filtered_words)
    nCr(K-5, 0, [])
    print(answer)


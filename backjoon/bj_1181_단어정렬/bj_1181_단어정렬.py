'''
1. 입력단어의 길이를 인덱스로 하는 2차원 배열(words)을 만든다.
(예를 들어, 길이가 10인 단어는 모두 words[10]에 담겨있을 수 있도록 하기 위해)

2. words배열을 완성한다.

3. words를 순회(길이 순)하며(1차원 배열이 나옴), 중복값을 없애고 정렬한다(사전 순)
'''

# 1.
N = int(input())
words = [[] for _ in range(52)]

# 2.
for _ in range(N):
    word = input()
    n = len(word)
    words[n].append(word)

# 3.
for word in words:
    for elem in sorted(list(set(word))):
        print(elem)


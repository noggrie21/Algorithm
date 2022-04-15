# 다른 사람 코드 보고 최적화 시도
'''
1. readline 사용하기
2. set을 사용해서 처음부터 중복값 제거하고 입력받기
3. 정렬할 때, key=len을 사용하여 길이 정렬시키기(길이로 정렬할 수 있는 지 몰랐음..)
4. 개행이 필요할 때, join에 이스케이프 문자 활용하기
'''
import sys

N = int(input())
words = set()

for _ in range(N):
    words.add(sys.stdin.readline().rstrip())

words = sorted(sorted(list(words)), key=len)
print('\n'.join(words))
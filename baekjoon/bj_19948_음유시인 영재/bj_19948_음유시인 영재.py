def make_title(content, space, alphabet):
    old = ord(' ')
    i = 0
    N = len(content)
    title = ''

    while i < N:
        ascii = content[i]

        # 이전 기록과 다른 경우
        if old != ascii:

            # 스페이스 였을 때,
            if ascii == ord(' '):

                # 입력 가능 횟수가 0이면,
                if not space:
                    return -1   # (입력 불가로) 함수 종료

                # 입력할 수 있으면
                space -= 1      # 입력 가능 횟수 차감
                old = ascii     # 이전 기록 갱신

            # 문자였을 때,
            else:

                # 소문자인 경우 대문자 코드로 변환(해당 알파벳 입력 가능한지 확인하기 위해 통일)
                if ascii >= ord('a'):
                    ascii -= ord('a') - ord('A')

                # 입력 횟수가 남지 않았으면,
                if not alphabet[ascii]:
                    return -1   # 함수 종료

                # 시의 제목으로
                if old == ord(' '):
                    title += chr(ascii)
                    content.append(ascii)
                    N += 1

                alphabet[ascii] -= 1
                old = content[i]

        i += 1

    return title


content = list(map(lambda x: ord(x), input()))
space = int(input())
alphabet = [0] * 65 + list(map(int, input().split()))

print(make_title(content, space, alphabet))
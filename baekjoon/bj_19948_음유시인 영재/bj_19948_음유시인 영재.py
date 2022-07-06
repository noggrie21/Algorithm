def make_title(content, space, alphabet):
    old = 32
    i = 0
    N = len(content)
    title = ''

    while i < N:
        ascii = content[i]

        # 이전 기록과 다른 경우
        if old != ascii:

            # 스페이스 였을 때,
            if ascii == 32:

                # 입력 횟수가 남지 않았으면,
                if not space:
                    return -1   # 함수 종료

                # 남았다면
                space -= 1      # 입력 가능 횟수 차감
                old = ascii     # 이전 기록 갱신

            # 문자였을 때,
            else:

                # 소문자인 경우 대문자 코드로 변환(해당 알파벳 입력 가능한지 확인하기 위해 통일)
                if ascii >= 97:
                    ascii -= 32

                if not alphabet[ascii]:
                    return -1

                if old == 32:
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
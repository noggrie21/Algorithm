def make_title(content, alphabet):
    title = ''
    old = -1

    for letter in content:
        print(letter, old, alphabet[letter])
        if old == letter:
            continue

        elif old != letter and alphabet[letter]:
            title += chr(letter+65)
            alphabet[letter] -= 1
            old = letter

        else:
            return -1

    return title


content = list(map(lambda x: ord(x), input()))
# title = list(map(lambda x: ord((x[0].upper())) - 65, input().split()))
space = int(input())
alphabet = list(map(int, input().split()))

print(content, space)
English = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(list(zip(English, alphabet)))

if space + 1 < len(content):
    print(-1)
else:
    print(make_title(content, alphabet))
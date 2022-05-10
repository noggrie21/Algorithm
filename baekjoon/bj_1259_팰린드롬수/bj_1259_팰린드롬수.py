def check():
    re_words = list(reversed(words))
    result = 'no'
    if words == re_words:
        result = 'yes'
    print(result)


words = list(input())
while words != ['0']:
    check()
    words = list(input())
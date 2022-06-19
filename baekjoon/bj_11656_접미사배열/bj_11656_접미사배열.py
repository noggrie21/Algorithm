word = input()
lst = sorted([word[i:] for i in range(len(word))])
for word in lst:
    print(word)

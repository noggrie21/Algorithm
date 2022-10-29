alphabet = [0] * 26

for char in input():
  alphabet[ord(char)-ord('a')] += 1

print(*alphabet)
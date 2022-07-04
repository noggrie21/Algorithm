import sys

N = int(input())

file_dict = {}

for _ in range(N):
    dum, extension = sys.stdin.readline().rstrip().split('.')

    if not file_dict.get(extension):
        file_dict[extension] = 1
    else:
        file_dict[extension] += 1

for key, value in sorted(file_dict.items()):
    print(key, value)

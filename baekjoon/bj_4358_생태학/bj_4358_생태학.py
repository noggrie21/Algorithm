import sys

kinds = {}
total = 0
tree = sys.stdin.readline().rstrip()

while tree:
  total += 1
  if kinds.get(tree):
        kinds[tree] += 1
  else:
      kinds[tree] = 1
  tree = sys.stdin.readline().rstrip()
sorted_kinds = sorted(list(kinds))

for kind in sorted_kinds:
  print(kind, f'{kinds[kind]/total * 100:0.4f}')

T = 1
flag = True

while flag:
  N = int(input())
  if not N:
    break

  students = [0] * (N+1)
  checked = [0] * (N+1)

  for i in range(1, N+1):
    students[i] = input()

  for _ in range(2*N -1):
    num, *status = input().split()
    checked[int(num)] += 1
  
  for i in range(1, N+1):
    if checked[i] == 1:
      print(T, students[i])
  T += 1

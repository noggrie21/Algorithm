from collections import deque
from sys import stdin

N = int(input())
arr = deque()

# lst = deque()
# lst.append(123)
# lst.append(555)
# print(lst)
# print(len(lst))


for _ in range(N):
    order, *num = stdin.readline().rstrip().split()
    # print(_, arr, order, num)

    if num:
        num = int(num[0])
        if order[5] == 'f':
            arr.appendleft(num)
        else:
            arr.append(num)

    elif order[0] == 's':
        print(len(arr))

    elif order[0] == 'e':
        if arr:
            print(0)
        else:
            print(1)

    elif not arr:
        print(-1)

    else:
        if order == 'front':
            print(arr[0])
        elif order == 'back':
            print(arr[-1])
        elif order == 'pop_front':
            print(arr.popleft())
        else:
            print(arr.pop())




    # elif order[0] == 'p':
    #     if not arr:
    #         print(-1)
    #     elif order[4] == 'f':
    #         print(arr.popleft())
    #     else:
    #         print(arr.pop())
    #
    # else:
    #     if order[0] == 's':
    #         print('size', len(arr))
    #     elif order[0] == 'e':
    #         if not arr:
    #             print(0)
    #         else:
    #             print(1)
    #     elif order[0] == 'f':
    #         if not arr:
    #             print(-1)
    #         else:
    #             print(arr[0])
    #     else:
    #         print(arr[-1])
    #         if not arr:
    #             print(-1)
    #         else:
    #             print(arr[-1])






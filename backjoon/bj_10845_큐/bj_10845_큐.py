def mypush():
    global rear
    global size
    global inputlst
    print(arr)
    print(inputlst)
    arr[rear] = inputlst[1]
    rear += 1
    size += 1


def mypop():
    global front
    global size

    if not size:
        print(-1)
        return
    front += 1
    size -= 1
    print(arr[front])


def myempty():
    if not size:
        print(1)
        return
    print(0)



def myfront():
    global front
    if not size:
        print(-1)
        return
    print(arr[front])


def myback():
    global rear
    if not size:
        print(-1)
        return
    print(arr[rear])



N = int(input())
arr = [0] * 10000
front = -1
rear = 0
size = 0
# method = {
#     'h': mypush(),
#     'p': mypop(),
#     'e': size,
#     'y': myempty(),
#     't': myfront(),
#     'k': myback(),
# }

for _ in range(N):
    method = {
        'h': mypush(),
        'p': mypop(),
        'e': size,
        'y': myempty(),
        't': myfront(),
        'k': myback(),
    }

    inputlst = input().split()
    char = inputlst[0][-1]
    method[char]





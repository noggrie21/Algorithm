def make_same(small, big, small_q, big_q):
    entirety = small_q + big_q
    half = (small + big) // 2

    n = len(small_q)
    front, rear = -1, n - 1

    cnt = 0

    while front != rear and rear < 2 * n - 1 and small != half:
        if small < half:
            rear += 1
            small += entirety[rear]
        else:
            front += 1
            small -= entirety[front]
        cnt += 1

    if small == half:
        return cnt
    return -1


def solution(queue1, queue2):
    amswer = -2
    small, big = sum(queue1), sum(queue2)

    if big < small:
        answer = make_same(big, small, queue2, queue1)
    elif big == small:
        answer = 0
    else:
        answer = make_same(small, big, queue1, queue2)

    return answer
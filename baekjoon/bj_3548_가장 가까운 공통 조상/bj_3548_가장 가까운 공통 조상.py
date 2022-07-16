def search_parents(child, parents):
    result = [child]

    while parents[child]:
        result.append(parents[child])
        child = parents[child]

    return result


def search_common(A_parents, B_parents):
     for a in A_parents:
         for b in B_parents:
             if a == b:
                 return a


T = int(input())

for _ in range(T):
    N = int(input())
    parents = [0] * (N+1)

    for _ in range(N-1):
        p, c = map(int, input().split())
        parents[c] = p

    A, B = map(int, input().split())

    A_parents = search_parents(A, parents)
    B_parents = search_parents(B, parents)
    ans = search_common(A_parents, B_parents)

    print(ans)

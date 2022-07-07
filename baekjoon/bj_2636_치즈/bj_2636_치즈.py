def search_edges(R, C):
    edges = []
    for r in range(R):
        for c in range(C):
            if not r * c or R - 1 == r or C - 1 == c:
                edges.append((r, c))

    return edges


R, C = map(int, input().split()) # R: 행, C: 열

edges = search_edges(R, C)

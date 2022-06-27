def DFS(level, cnt, songs):
    global answer

    # 종료 파트
    if level > N:

        return

    # 유도 파트
    # 1. 포함
    DFS(level+1, cnt+1, songs|songs[level])

    # 2. 미포함
    DFS(level+1, cnt, songs)

N, M = map(int, input().split())
playlist = []
answer = -1
name, possibility = input().split()

song = list(map(lambda x: '1' if x == 'Y' else '0', possibility))
playlist.append(int(''.join(song)))

DFS(0, 0, 0)
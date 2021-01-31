# code 10.3

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    G[a].append(b)

    # 無向グラフなら
    # G[b].append(a)
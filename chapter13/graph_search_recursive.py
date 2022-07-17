# code 13.2
from graph import Graph

seen = []


def dfs(G: Graph, v: int):
    seen[v] = True

    for next_v in G[v]:
        if seen[next_v]:
            continue

        dfs(G, next_v)


N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    G[a].append(b)

seen = [False] * N
for v in range(N):
    if seen[v]:
        continue

    dfs(G, v)

# code 13.3
from typing import List
from graph import Graph


def bfs(G: Graph, s: int) -> List[int]:
    N = len(G)
    dist = [-1] * N
    que = []

    dist[0] = 0
    que.append(0)

    while len(que) != 0:
        v = que.pop()
        for x in G[v]:
            if dist[x] != -1:
                continue
            dist[x] = dist[v] + 1
            que.append(x)

    return dist


N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = bfs(G, 0)

for v in range(N):
    print(f"v: {dist[v]}")

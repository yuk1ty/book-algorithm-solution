# code 13.5
from typing import List
from graph import Graph

color = []


def dfs(G: Graph, v: int, cur: int = 0) -> bool:
    color[v] = cur
    for next_v in G[v]:
        if color[next_v] != -1:
            if color[next_v] == cur:
                return False
            continue

        if not dfs(G, next_v, 1 - cur):
            return False

    return True


N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

color = [-1] * N

is_bipartite = True

for v in range(N):
    if color[v] != -1:
        continue
    if not dfs(G, v):
        is_bipartite = False

if is_bipartite:
    print("Yes")
else:
    print("No")

# code 13.4
from typing import List
from graph import Graph

seen: List[bool] = []


def dfs(G: Graph, v: int):
    seen[v] = True

    for next_v in G[v]:
        if seen[next_v]:
            continue

        dfs(G, next_v)


N, M, s, t = map(int, input().split())

G = [] * N

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

seen = [False] * N
dfs(G, s)

if seen[t]:
    print("Yes")
else:
    print("No")

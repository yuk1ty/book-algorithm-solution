# code 13.6
from typing import List
from graph import Graph

seen = []
order = []


def rec(G: Graph, v: int):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        rec(G, next_v)

    order.append(v)


N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

seen = [False] * N
order.clear()

for v in range(N):
    if seen[v]:
        continue
    rec(G, v)

order.reverse()

for v in order:
    print(f"{v} ->")

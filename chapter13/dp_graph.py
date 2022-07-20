# code 13.9
from typing import List
from graph import Graph

depth = []
subtree_size = []


def dfs(G: Graph, v: int, p: int = -1, d: int = 0):
    depth[v] = d
    for c in G[v]:
        if c == p:
            continue
        dfs(G, c, v, d + 1)

    subtree_size[v] = 1
    for c in G[v]:
        if c == p:
            continue
        subtree_size[v] += subtree_size[c]


N = int(input())

G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

root = 0
depth = [0] * N
subtree_size = [0] * N
dfs(G, root)

for v in range(N):
    print(f"{v}: depth = {depth[v]}, subtree_size = {subtree_size[v]}")

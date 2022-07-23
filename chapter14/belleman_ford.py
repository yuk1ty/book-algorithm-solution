from dataclasses import dataclass
import math
from typing import List


INF = math.inf


@dataclass
class Edge:
    to: int
    w: int


Graph = List[List[Edge]]


def chmin(a: float, b: float) -> bool:
    if a > b:
        a = b
        return True
    else:
        return False


N, M, s = map(int, input().split())

G: Graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, input().split())
    G[a].append(Edge(b, w))

exist_negative_cycle = False

dist = [math.inf] * N
dist[s] = 0

for iter in range(0, N):
    update = False
    for v in range(0, N):
        if dist[v] == INF:
            continue

        for e in G[v]:
            if chmin(dist[e.to], dist[v] + e.w):
                update = True

    if not update:
        break

    if iter == N - 1 and update:
        exist_negative_cycle = True

if exist_negative_cycle:
    print("NEGATIVE CYCLE")
else:
    for v in range(0, N):
        if dist[v] < INF:
            print(dist[v])
        else:
            print("INF")

# code 14.4
from dataclasses import dataclass
import io
import math
from typing import List
from queue import PriorityQueue


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

dist = [INF] * N
dist[s] = 0

que = PriorityQueue()
que.put((dist[s], s))

while que.not_empty:
    poped = que.get()
    v = poped[1]
    d = poped[0]

    if d > dist[v]:
        continue

    for e in G[v]:
        if chmin(dist[e.to], dist[v] + e.w):
            que.put((dist[e.to], e.to))

for v in range(N):
    if dist[v] < INF:
        print(dist[v])
    else:
        print("INF")

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

used = [False] * N
dist = [INF] * N

for iter in range(N):
    min_dist = INF
    min_v = -1

    for v in range(N):
        if not used[v] and dist[v] < min_dist:
            min_dist = dist[v]
            min_v = v

    if min_v == -1:
        break

    for e in G[min_v]:
        chmin(dist[e.to], dist[min_v] + e.w)

    used[min_v] = True

	for v in range(N):
		if dist[v] < INF:
			print(dist[v])
		else:
			print("INF")

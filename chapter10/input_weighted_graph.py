# code 10.4

from dataclasses import dataclass

@dataclass
class Edge:
    to: int
    w: int


N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, input().split())
    G[a].append(Edge(b, w))

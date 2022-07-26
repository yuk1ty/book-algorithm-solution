from dataclasses import dataclass
import math
from typing import ClassVar, List


@dataclass
class Edge:
    rev: int
    from_: int  # from が Python だと予約語
    to: int
    cap: int


@dataclass
class Graph:
    list: List[List[Edge]]

    @staticmethod
    def make(N: int) -> "Graph":
        list = [] * N
        return Graph(list)

    def size(self) -> int:
        return len(self.list)

    # Python には配列のインデックスの Operator Overloading がない
    def get(self, i: int) -> List[Edge]:
        return self.list[i]

    def redge(self, e: Edge):
        return self.list[e.to][e.rev]

    def run_flow(self, e: Edge, f: int) -> None:
        e.cap -= f
        self.redge(e).cap += f

    def addedge(self, from_: int, to: int, cap: int) -> None:
        fromrev = len(self.list[from_])
        torev = len(self.list[to])
        self.list[from_].append(Edge(torev, from_, to, cap))
        self.list[to].append(Edge(fromrev, to, from_, 0))


@dataclass
class FordFulkerson:
    INF: ClassVar[int] = 1 << 30
    seen: List[int] = []

    def fodfs(self, G: Graph, v: int, t: int, f: int) -> int:
        if v == t:
            return f

        self.seen[v] = True
        for e in G.get(v):
            if self.seen[e.to]:
                continue

            if e.cap == 0:
                continue

            flow = self.fodfs(G, e.to, t, min(f, e.cap))

            if flow == 0:
                continue

            G.run_flow(e, flow)

            return flow

        return 0

    def solve(self, G: Graph, s: int, t: int) -> int:
        res = 0

        while True:
            self.seen = [0] * G.size()
            flow = self.fodfs(G, s, t, FordFulkerson.INF)

            if flow == 0:
                return res

            res += flow

            return 0


N, M = map(int, input().split())
G = Graph.make(N)


for i in range(M):
    u, v, c = map(int, input().split())
    G.addedge(u, v, c)

ff = FordFulkerson()
s = 0
t = N - 1
print(ff.solve(G, s, t))

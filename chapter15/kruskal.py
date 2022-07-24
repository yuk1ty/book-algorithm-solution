# code 15.1

from dataclasses import dataclass
from typing import List


# code 11.3 からポート
@dataclass
class UnionFind:
    par: List[int]
    siz: List[int]

    @staticmethod
    def make(n: int) -> "UnionFind":
        return UnionFind(par=[-1] * n, siz=[1] * n)

    def root(self, x) -> int:
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]

        return True

    def size(self, x: int) -> int:
        return self.siz[self.root(x)]


Edge = (int, (int, int))

N, M = map(int, input().split())
edges = []

for i in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, (u, v)))

edges.sort()

res = 0
uf = UnionFind.make(N)

for i in range(M):
    w = edges[i][0]
    u = edges[i][1][0]
    v = edges[i][1][1]

    if uf.issame(u, v):
        continue

    res += w
    uf.unite(u, v)

print(res)

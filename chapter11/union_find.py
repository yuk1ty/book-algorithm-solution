# code 11.3

from dataclasses import dataclass
from typing import List


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


uf = UnionFind.make(7)

uf.unite(1, 2)
uf.unite(2, 3)
uf.unite(5, 6)

print(uf.issame(1, 3))
print(uf.issame(2, 5))

uf.unite(1, 6)
print(uf.issame(2, 5))

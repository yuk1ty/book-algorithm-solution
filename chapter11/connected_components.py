# code 11.4
from re import X
from union_find import UnionFind

N, M = map(int, input().split())

uf = UnionFind.make(N)

for i in range(M):
    a, b = map(int, input().split())
    uf.unite(a, b)

res = 0

for x in range(N):
    if uf.root(x) == x:
        res += 1

print(res)

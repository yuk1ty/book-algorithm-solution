# code 18.1
from typing import List


Graph = List[List[int]]
w = []
G = []
dp1 = []
dp2 = []


def dfs(v: int, p: int = -1) -> None:
    for ch in G[v]:
        if ch == p:
            continue
        dfs(ch, v)

    dp1[v] = 0
    dp2[v] = w[v]
    for ch in G[v]:
        if ch == p:
            continue
        dp1[v] += max(dp1[ch], dp2[ch])
        dp2[v] += dp1[ch]


N = int(input())

for i in range(N + 1):
    w[i] = int(input())

G.clear()

for i in range(N):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

root = 0
dp1 = [0] * N
dp2 = [0] * N
dfs(root)

print(max(dp1[root], dp2[root]))

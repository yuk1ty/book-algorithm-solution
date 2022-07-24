# code 14.5

import math


INF = math.inf


N, M = map(int, input().split())

dp = [[INF] * N] * N

for e in range(M):
    a, b, w = map(int, input().split())
    dp[a][b] = w

for v in range(N):
    dp[v][v] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

exist_negative_cycle = False

for v in range(N):
    if dp[v][v] < 0:
        exist_negative_cycle = True

if exist_negative_cycle:
    print("NEGATIVE CYCLE")
else:
    for i in range(N):
        for j in range(N):
            if j:
                print(" ")
            if dp[i][j] < INF // 2:
                dp[i][j]
            else:
                print("INF")

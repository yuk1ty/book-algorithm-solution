# code 5.7

from typing import TypeVar

T = TypeVar("T")

def chmax(a: T, b: T) -> int:
    if (a < b):
        return b
    else:
        return a

N = int(input())
W = int(input())

weight = [int(input()) for _ in range(N)]
value = [int(input()) for _ in range(N)]

dp = [[0] * W + 1 for _ in range(N + 1)]

for i in range(0, N + 1):
    for w in range(0, W + 1):
        # まだ余力がある場合は i 番目の品物を選択する
        if (w - weight[i] >= 0):
            dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w - weight[i]] + value[i])
        
        # i 番目の品物を選択しない場合は何も変化しない
        dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w])

print(dp[N][W])
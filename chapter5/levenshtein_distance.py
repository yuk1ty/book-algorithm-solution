# code 5.7

from typing import TypeVar

T = TypeVar("T")

def chmin(a: T, b: T) -> int:
    if (a > b):
        return b
    else:
        return a

S = str(input())
T = str(input())

dp = [[float("inf")] * (len(T) + 1) for _ in range(len(S) + 1)]

dp[0][0] = 0

for i in range(0, len(S) + 1):
    for j in range(0, len(T) + 1):
        if (i > 0 and j > 0):
            if (S[i - 1] == T[j - 1]):
                dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1] + 1)

        if (i > 0):
            dp[i][j] = chmin(dp[i][j], dp[i - 1][j] + 1)
        if (j > 0):
            dp[i][j] = chmin(dp[i][j], dp[i][j - 1] + 1)

print(dp[len(S)][len(T)])
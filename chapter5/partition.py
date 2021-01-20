# code 5.9

from typing import TypeVar

T = TypeVar("T")

def chmin(a: T, b: T) -> int:
    if (a > b):
        return b
    else:
        return a

N = int(input())

c = [[int(input())] for _ in range(N + 1)]

dp = [float("inf")] * (N + 1)

dp[0] = 0

for i in range(0, N + 1):
    for i in range(0, i + 1):
        chmin(dp[i], dp[j] + c[i][j])

print(dp[N])

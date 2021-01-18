# code 5.6

from typing import TypeVar

T = TypeVar("T")

dp = [float("inf")] * N
h = [] * N

def chmin(a: T, b: T) -> int:
    if (a > b):
        return b
    else:
        return a

def rec(i: int) -> int:
    if (dp[i] < float("inf")):
        return dp[i]
    
    # ベースケース: 足場のコスト0は0
    if (i == 0):
        return 0
    
    # 答えを表す変数を INF で初期化する
    res = float("inf")

    # 足場 i - 1 から来た場合
    chmin(res, rec(i - 1) + abs(h[i] - h[i - 1]))

    # 足場 i - 2 から来た場合
    if (i > 1):
        chmin(res, rec(i - 2) + abs(h[i] - h[i - 2]))
    
    # `:=` は Python 3.8 以降から導入されているセイウチ演算子。
    # 変数の代入と使用を同時にできる。
    return dp[i] := res

N = int(input())
h = [int(input()) for _ in range(N)]

print(rec(N - 1))

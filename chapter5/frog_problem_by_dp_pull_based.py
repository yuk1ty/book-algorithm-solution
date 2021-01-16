# code 5.4

# Python の場合は動的型付き言語なので、下記のように無理に型付けをする必要は必ずしもないかもしれない。
# 一応本書のテンプレート関数の導入を尊重して、typing モジュールを用いた型付けを行っている。

from typing import TypeVar

T = TypeVar("T")

# Python の場合、数値型のようなイミュータブルな値を関数に渡すと、関数内で代入する際にコピーが走るようになっている。
# このため、C++ のサンプルコードと同じ挙動はさせられない。
# なので、比較後にどちらかの値を返して、呼び出し元で再度配列に代入し直す。
def chmin(a: T, b: T) -> int:
    if (a > b):
        return b
    else:
        return a

N = int(input())
print(N)
h = [int(input()) for _ in range(N)]

dp = [float("inf")] * N

dp[0] = 0

for i in range(0, N):
    if (i + 1 < N):
        dp[i + 1] = chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
    if (i + 2 < N):
        dp[i + 2] = chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))

print(dp[N - 1])

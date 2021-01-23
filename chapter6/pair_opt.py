# code 6.4

import bisect

INF = 20_000_000

N = int(input())
K = int(input())

a = [int(input()) for _ in range(N)]
b = [int(input()) for _ in range(N)]

min_value = INF

b.sort()

b.append(INF)

for i in range(N):
    # std::lower_bound の代わりに Python では bisect.bisect_left が使用できる。
    # この関数は C++ とは違い、イテレータではなくインデックスを返すので、
    # index という変数名に変更している。
    index = bisect.bisect_left(b, K - a[i])

    # 挿入可能な位置の値を取り出す
    val = b[index]

    if (a[i] + val < min_value):
        min_value = a[i] + val

print(min_value)

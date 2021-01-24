# code 7.2

from typing import TypeVar, Tuple, List

# pair を実装する
T = TypeVar("T")
Pair = Tuple[T, T]

Interval = Pair[int]

# 下記は C++ の pair っぽく取り出せるように書いている
first = 0
second = 1

# 終端時刻で大小比較する関数。
# Python の場合は、sorted という組み込みの関数に比較関数を渡すと比較をカスタマイズできる。
# この比較関数は「比較のキーをどれにするか」を対象とするので、下記のような実装になる。
# (この問題では終端時刻 = Pair の2つ目を取り出す)
def cmp(val: Interval) -> int:
    return val[second]

N = int(input())

# TODO たぶんスペース区切りで本来は書くので、これは調整する
inter: List[Interval] = [(int(input()), int(input())) for _ in range(N)]

# 終端時刻が早い順にソートする
inter = sorted(inter, key=cmp)

# 貪欲に選ぶ
res = 0
current_end_time = 0

for i in range(N):
    if (inter[i][first] < current_end_time):
        continue

    res += 1

    current_end_time = inter[i][second]

print(res)


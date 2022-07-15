# code 12.4
# バケットソートのイメージとしては、この動画がわかりやすかった。
# https://www.youtube.com/watch?v=VuXbEb5ywrU

from typing import List

MAX = 100_000

def bucket_sort(a: List[int]):
	N = len(a)

	num = [0] * MAX
	for i in range(N):
		num[a[i]] += 1
	
	sum = [0] * MAX
	for v in range(1, MAX):
		sum[v] = sum[v - 1] + num[v]

	a2 = [0] * N
	for i in range(N - 1, -1, -1):
		sum[a[i]] -= 1
		a2[sum[a[i]]] = a[i]
	
	a = a2

N = int(input())
a = list(map(int, input().split()))

# TODO 動作確認
bucket_sort(a)
print(a)

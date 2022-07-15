# code 12.4

from typing import List

def heapify(a: List[int], i: int, N: int):
	childl = i * 2 + 1

	if childl >= N:
		return
	
	if childl + 1 < N and a[childl + 1] > a[childl]:
		childl += 1
	
	if a[childl] <= a[i]:
		return
	
	a[i], a[childl] = a[childl], a[i]

	heapify(a, childl, N)

def heap_sort(a: List[int]):
	N = len(a)

	for i in range(N // 2 - 1, -1, -1):
		heapify(a, i, N)
	
	for i in range(N - 1, 0, -1):
		a[0], a[i] = a[i], a[0]
		heapify(a, 0, i)

N = int(input())
a = list(map(int, input().split()))

heap_sort(a)
print(a)

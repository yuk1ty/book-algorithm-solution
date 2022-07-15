# code 12.3

from typing import List

def quick_sort(a: List[int], left: int, right: int):
	if right - left <= 1:
		return
	
	pivot_index = (left + right) // 2
	pivot = a[pivot_index]
	a[pivot_index], a[right - 1] = a[right - 1], a[swap_index]

	i = left
	for j in range(left, right - 1):
		if a[j] < pivot:
			a[i], a[j] = a[j], a[i]
			i += 1
	
	a[i], a[right - 1] = a[right - 1], a[i]

	quick_sort(a, left, i)
	quick_sort(a, i + 1, right)


N = int(input())
a = list(map(int, input().split()))

quick_sort(a, 0, N)

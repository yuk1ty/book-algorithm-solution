# code 12.2

from typing import List

def merge_sort(a: List[int], left: int, right: int):
	if right - left == 1:
		return
	
	mid = left + (right - left) // 2

	merge_sort(a, left, mid)
	merge_sort(a, mid, right)

	buf = []

	[buf.append(a[i]) for i in range(left, mid)]
	# TODO for 
	j = right - 1
	while j >= mid:
		buf.append(a[j])
		j -= 1
	
	index_left = 0
	index_right = len(buf) - 1

	for i in range(left, right):
		if buf[index_left] <= buf[index_right]:
			a[i] = buf[index_left]
			index_left += 1
		else:
			a[i] = buf[index_right]
			index_right -= 1

N = int(input())
a = list(map(int, input().split()))

merge_sort(a, 0, N)

print(a)

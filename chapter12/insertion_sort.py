from typing import List

def insertion_sort(a: List[int]):
    N = len(a)
    for i in range(N):
        v = a[i]

        j = i
        while j > 0:
            if a[j-1] > v:
                a[j] = a[j - 1]
                j -= 1
            else:
                break
        a[j] = v

N = int(input())
a = list(map(int, input().split()))

insertion_sort(a)
print(a)

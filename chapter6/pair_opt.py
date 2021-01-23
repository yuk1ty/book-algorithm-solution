# code 6.4

N = int(input())
K = int(input())

a = [int(input()) for _ in range(N)]
b = [int(input()) for _ in range(N)]

min_value = float("inf")

b.sort()

b.append(float("inf"))


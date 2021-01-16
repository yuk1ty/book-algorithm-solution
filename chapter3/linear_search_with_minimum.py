# code 3.3

INF = 20_000_000

N = int(input())
a = [int(input()) for _ in range(N)]

min_value = INF
for i in range(N):
    if (a[i] < min_value):
        min_value = a[i]

print(min_value)
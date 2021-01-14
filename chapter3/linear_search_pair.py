INF = 20_000_000

N = int(input())
K = int(input())

a = [int(input()) for _ in range(N)]
b = [int(input()) for _ in range(N)]

min_value = INF

for i in range(N):
    for j in range(N):
        if (a[i] + b[j] < K):
            continue
        
        if (a[i] + b[j] < min_value):
            min_value = a[i] + b[j]

print(min_value)
N = int(input())
print(N)

h = [int(input()) for _ in range(N)]

dp = [float("inf")] * N

dp[0] = 0

for i in range(1, N):
    if (i == 1):
        dp[i] = abs(h[i] - h[i - 1])
    else:
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))

print(dp[N - 1])
# code 3.5

N = int(input())
W = int(input())

a = [int(input()) for _ in range(N)]

exist = False

for bit in range(1 << N):
    sum = 0

    for i in range(N):
        if (bit & (1 << i)):
            sum += a[i]

    if (sum == W):
        exist = True

if (exist):
    print("Yes")
else:
    print("No")
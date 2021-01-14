N = int(input())
v = int(input())
a = [int(input()) for _ in range(N)]

exist = False
for i in range(N):
    if (a[i] == v):
        exist = True

if (exist):
    print("Yes")
else:
    print("No")
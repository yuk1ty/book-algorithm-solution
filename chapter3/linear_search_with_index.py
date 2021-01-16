# code 3.2

N = int(input())
v = int(input())
a = [int(input()) for _ in range(N)]

found_id = None
for i in range(N):
    if (a[i] == v):
        found_id = i
        break

print(found_id)
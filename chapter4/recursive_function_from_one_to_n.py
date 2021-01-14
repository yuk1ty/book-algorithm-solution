# code 4.1
def func(N: int) -> int:
    if N == 0:
        return 0
    return N + func(N - 1)

# 本の中にはないですが便利なので
ans = func(5)
print(ans)
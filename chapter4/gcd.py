# code 4.4

# GCD(m, n) = GCD(n, r)
def GCD(m: int, n: int) -> int:
    if (n == 0):
        return m

    # r = m % n
    return GCD(n, m % n)

print(GCD(51, 15)) # 3
print(GCD(15, 51)) # 3
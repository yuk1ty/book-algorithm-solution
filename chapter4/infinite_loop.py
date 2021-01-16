# code 4.3

# これはループが止まらない。
def func(N: int) -> int:
    if (N == 0):
        return 0
    
    return N + (N + 1)
# code 4.5

def fibo(N: int) -> int:
    if (N == 0):
        return 0
    elif (N == 1):
        return 1

    return fibo(N - 1) + fibo(N - 2)

print(fibo(8)) # 21
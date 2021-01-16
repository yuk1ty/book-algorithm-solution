# code 4.2

def func(N: int) -> int:
    print(f"func({N}) を呼び出しました")

    if (N == 0):
        return 0
    
    result = N + func(N - 1)
    print(f"{N}までの和 = {result}")

    return result

func(5)
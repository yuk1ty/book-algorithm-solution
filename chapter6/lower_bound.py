# code 6.2

def P(x: int) -> bool:
    pass

def binary_search():
    left = None # 何かしらの値
    right = None # 何かしらの値

    while (right - left > 1):
        mid = left + (right - left) // 2
        if (P(mid)):
            right = mid
        else:
            left = mid
        
    return right
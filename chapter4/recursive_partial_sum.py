# code 4.9

from typing import List

def func(i: int, w: int, a: List[int]) -> bool:
    if (i == 0):
        if (w == 0):
            return True
        else:
            return False
    
    # a[i - 1] を選ばない場合
    if (func(i - 1, w, a)):
        return True
    
    # a[i - 1] を選ぶ場合
    if (func(i - 1, w - a[i - 1], a)):
        return True
    
    return False

N = int(input())
W = int(input())

a = [int(input()) for _ in range(N)]

if (func(N, W, a)):
    print("Yes")
else:
    print("No")
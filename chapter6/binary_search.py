# code 6.1

N = 8
a = [3, 5, 8, 10, 14, 17, 21, 39]

def binary_search(key: int) -> int:
    left = 0
    right = len(a) - 1

    while (right >= left):
        # Python では通常の除算 `/` をすると、型が float になる。
        # 回避策は、`int()` で囲ってキャストするか、
        # 下記のように整数除算用の演算子 `//` を使用すると int のままにできる。
        mid = left + (right - left) // 2
        if (a[mid] == key):
            return mid
        elif(a[mid] > key):
            right = mid - 1
        elif(a[mid] < key):
            left = mid + 1
    
    return -1

print(binary_search(10))
print(binary_search(3))
print(binary_search(39))

print(binary_search(-100))
print(binary_search(9))
print(binary_search(100))
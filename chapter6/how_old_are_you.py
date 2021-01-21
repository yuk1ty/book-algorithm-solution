print("Start Game!")

left = 20
right = 36

while (right - left > 1):
    mid = left + (right - left) // 2

    print(f"Is the age less than {mid} ? (yes / no)")

    ans = str(input())

    if (ans == "yes"):
        right = mid
    else:
        left = mid

print(f"The age is {left} !")
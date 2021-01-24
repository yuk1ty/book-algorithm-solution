# code 7.1

value = [500, 100, 50, 10, 5, 1]

X = int(input())
a = [int(input()) for _ in range(6)]

result = 0

for i in range(6):
    add = X // value[i]

    if (add > a[i]):
        add = a[i]
    
    X -= value[i] * add

    result += add

print(result)
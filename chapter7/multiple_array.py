# code 7.3

N = int(input())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(N)]

sum = 0

# range 関数の第3引数は実はどういった方法で i を計算するかのステップを指定できる。
for i in range(N, 0, -1):
    A[i] += sum
    amari = A[i] % B[i]
    D = 0
    if (amari != 0):
        D = B[i] - amari
    sum += D

print(sum)
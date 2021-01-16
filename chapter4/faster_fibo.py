# code 4.7

F = list()
F.append(0)
F.append(1)

for N in range(2, 50):
    F.append(F[N - 1] + F[N - 2])
    print(f"{N} 項目: {F[N]}")
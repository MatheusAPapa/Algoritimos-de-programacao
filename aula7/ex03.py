n = int(input('Digite o valor de n: '))
s = 0
for i in range(0, n, 3):
    s += i
s += 3 * n - 1
print(f'S = {s}')
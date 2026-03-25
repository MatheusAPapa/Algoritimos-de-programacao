num = float(input('Digite um número: '))
while num > 0:
    num -= 1
    if num % 4 == 0:
        print(f'O número {num} é divisível por 4')
    
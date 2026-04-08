def primo (n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

num = int(input('Digite um número: '))
continuar = 1
while continuar == 1:
    if primo(num) == True:
        print(f'O número {num} é primo')
    else:
        print(f'O número {num} não é primo')
    continuar = int(input('Deseja continuar tentando[1 - sim; 2 - não]? '))
    if continuar == 1:
        num = int(input('Digite outro número: '))
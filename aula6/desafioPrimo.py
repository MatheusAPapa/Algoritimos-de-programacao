num = int(input('Digite um número: '))
def primo (n):
#se for 1, 0,  ou negativo não é primo
    if n <= 1:
        return False
#nenhum par é primo, menos o 2
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
#Só precisa testar divisores até raiz n, pois se um número tiver divisor maior que raiz de n, já existiria um menor antes. 
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
if primo(num) == True:
    print('é primo')
else:
    print('não é primo')
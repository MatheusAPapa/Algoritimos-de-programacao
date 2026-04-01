num = int(input('Digite um número: '))
def somaInteiros (n):
    soma = 0
    while n > 0:
        soma += n % 10
        n //= 10
    return soma
def maiorNum (n):
    maior = 0
    while n > 0:
        num = n % 10
        if num > maior:
            maior = num
        n //= 10
    return maior

print(f'A soma do snúmeros é {somaInteiros(num)} e o maior dígito é {maiorNum(num)}')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
def somaIntervalo (n1, n2):
    for i in range(n1, n2 + 1):
        soma += i
    return soma
print(somaIntervalo(num1, num2))
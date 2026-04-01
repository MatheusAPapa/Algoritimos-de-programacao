def lerNum ():
    n = float(input('Digite um número: '))
    return n

def soma (n1, n2, n3):
    resultado = n1 + n2 + n3
    return resultado

num1 = lerNum()
num2 = lerNum()
num3 = lerNum()
soma = soma(num1, num2, num3)
print(f' a soma dos três números é {soma}')
salario = float(input('Digite o seu salário: '))
if salario < 500:
    salario *= 1.15
else:
    if 500 <= salario <= 1000:
        salario *= 1.10
    else:
        salario *= 1.05
print(salario)
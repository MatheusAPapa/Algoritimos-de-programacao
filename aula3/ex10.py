salario = float(input('Digite o seu salário: '))
if salario <= 1500:
    salario *= 1.15
else:
    if 1500 < salario <= 3000:
        salario *= 1.10
    else:
        salario *= 1.05
print(salario)
salario = float(input('Qual o salário do funcionário: '))
plano = int(input('Qual o plano de trabalho do funcionário: '))
if plano == 1:
    salario *= 1.1
    print(f'Salário após reajuste: {salario}')
elif plano == 2:
    salario *= 1.15
    print(f'Salário após reajuste: {salario}')
elif plano == 3:
    salario *= 1.2
    print(f'Salário após reajuste: {salario}')
else:
    print('Plano inválido')

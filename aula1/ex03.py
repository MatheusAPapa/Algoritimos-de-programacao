salario = int(input('Digite o valor do seu salário mensal: '))
reajuste = int(input('Digite o valor do reajuste: '))
print(f'O valor do salário após o reajuste é {salario * (1 + (reajuste / 100))}')

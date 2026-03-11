salarioB = float(input('Digite o valor do seu salário bruto: '))
prest = float(input('Digite o valor da prestação: '))
if prest > salarioB * 0.3:
    print('Emprestímo negado')
else:
    temp = int(input('Quantos anos será o tempo de serviço? '))
    if temp > 2:
        print('Emprestímo aprovado com bonûs')
    else:
        print('Empréstimo aprovado')
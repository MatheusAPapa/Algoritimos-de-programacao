num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print('''
===========================
    Escolha a operação
===========================
1 - média dos números
2 - diferença entre o meior e o menor
3 - produto dos números
4 - divisão do primeiro pelo segundo
''')
menu = int(input('Qual operação será realizada? '))
match menu:
    case 1:
        print(f'A média é {(num1 + num2) / 2}')
    case 2:
        if num1 > num2:
            print(f'A diferença entre o maior e o menor é {num1 - num2}')
        else: 
            print(f'A diferença entre o maior e o menor é {num2 - num1}')
    case 3:
        print(f'O produto dos números é {num1 * num2}')
    case 4:
        print(f'A divisão do primeiro pelo segundo é {num1 / num2}')
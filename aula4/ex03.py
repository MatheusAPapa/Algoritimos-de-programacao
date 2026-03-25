a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite outro número: '))
if a == b == c:
    print('Todos são iguais')
elif a > b:
    if b > c:
        print(f'Ordenando os números fica {a, b, c}')
    elif c > a:
        print(f'Ordenando os números fica {c, a, b}')
    else:
        print(f'Ordenando os números fica {a, c, b}')
elif b > a:
    if a > c:
        print(f'Ordenando os números fica {b, a, c}')
    elif c > b:
        print(f'Ordenando os números fica {c, b, a}')
    else:
        print(f'Ordenando os números fica {b, c, a}')
else:
    #c será a maior
    if a > b:
        print(f'Ordenando os números fica {c, a, b}')
    else:
        print(f'Ordenando os números fica {c, b, a}')

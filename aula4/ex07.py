cod = int(input('Digite o código do produto: '))
match cod:
    case 1:
        print('Alimento não perecível')
    case 2 | 3 | 4:
        print('Alimento perecível')
    case 5 | 6:
        print('Vestuário')
    case 7:
        print('Higiene pessoal')
    case 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15:
        print('Limpeza e utencílios')
    case _:
        print('Código inválido')
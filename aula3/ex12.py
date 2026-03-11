a = float(input('Digite o valor 1º do lado: '))
b = float(input('Digite o valor 2º do lado: '))
c = float(input('Digite o valor 3º do lado: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c: 
        print('Triângulo equilátero')
    else:
        if a == b or a == c or b == c:
            print('Triângulo isócelis')
        else:
            print('Triângulo escaleno')
else:
    print('Esse triângulo não existe')
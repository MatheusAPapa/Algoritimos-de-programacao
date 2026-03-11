print('''
Sistema linar nessa ordem:
    ax + by = c
    dx + ey = f
''')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
d = float(input('Digite o valor de d: '))
e = float(input('Digite o valor de e: '))
f = float(input('Digite o valor de f: '))

if (a * e) - (b * d) != 0:
    x = (c * e - b * f) / (a * e - b * d)
    y = (a * f - c * d) / (a * e - b * d)    
    print(f'O valor de x é {x} e o de y é {y}')
else: 
    print('Esse sistema não tem solução')
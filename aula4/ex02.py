x = float(input('Digite o valor de "x" do intervalo [x, y]: '))
y = float(input('Digite o valor de "y" do intervalo [x, y]: '))
z = float(input('Digite um número para verificar se está no intervalo: '))
if x <= z <= y:
    print(f'O número {z} está no intervalo [{x}, {y}]')
else:
    print(f'O número {z} não está no intervalo [{x}, {y}]')
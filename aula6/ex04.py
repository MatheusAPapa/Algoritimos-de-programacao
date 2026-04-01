a = int(input('Digite o valor de a para o intervalo [a, b]: '))
b = int(input('Digite o valor de b para o intervalo [a, b]: '))
def parImparNoIntervalo (x, y):
    if x > y:
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i)
    else:
        for i in range(y, x + 1):
            if i % 2 == 0:
                print(i)

parImparNoIntervalo(a, b)
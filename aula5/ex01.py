num = float(input('Digite um número: '))
cont0_25 = 0
cont26_50 = 0
cont51_75 = 0
cont76_100 = 0
foraIntervalo = 0
while num >= 0:
    if num <= 25:
        cont0_25 += 1
    elif num <= 50:
        cont26_50 += 1
    elif num <= 75:
        cont51_75 += 1
    elif num <= 100:
        cont76_100 += 1
    else:
        foraIntervalo += 1
print(f'''
Você digitou {cont0_25} números no intervalo [0, 25]
Você digitou {cont0_25} números no intervalo [26, 50]
Você digitou {cont26_50} números no intervalo [51, 75]
Você digitou {cont76_100} números no intervalo [76, 100]
Você digitou {foraIntervalo} números fora dos intervalos acima
''')
autonomia = 12
tempo = float(input('Qual o tempo gasto na estrada (em h)? '))
velocidadeMedia = int(input('Qual a velociade média que você estava dirigindo (em km)? '))
distancia = velocidadeMedia * tempo
consumo = distancia / autonomia
print(f'''
Você ficou {tempo} na estrada e andou cm uma velocidade média de {velocidadeMedia}Km/h, percorrendo uma distância de {distancia}km.
O consumo de combustível foi de {consumo}
''')
parafuso = float(input('Digite o valor do parafuso: '))
porca = float(input('Digite o valor da porca: '))
aruela = float(input('Digite o valor da aruela: '))

cliente = str(input('Digite o nome do cliente: '))

qntParafuso = int(input('Digite quantos parafusos o cliente comprou: '))
qntPorca = int(input('Digite quantos porcas o cliente comprou: '))
qntAruela = int(input('Digite quantos aruelas o cliente comprou: '))

print(f''' 
Cliente: {cliente}
Valor da compra: {(parafuso * 0.9) * qntParafuso + (porca * 0.8) * (qntPorca + aruela * 0.7) * qntAruela}
Itens:
    Parafusos: {qntParafuso}
    Porcas: {qntPorca}
    Aruela: {qntAruela}
''')
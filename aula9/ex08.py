a = str(input("Telefonou para a vítima? "))
b = str(input("Esteve no local do crime? "))
c = str(input("Mora perto da vítima? "))
d = str(input("Devia para a vítima? "))
e = str(input("Já trabalhou com a vítima? "))
respostas = []
if a in ['s', 'S', 'Sim', 'sim']:
    respostas.append(a)
if b in ['s', 'S', 'Sim', 'sim']:
    respostas.append(b)
if c in ['s', 'S', 'Sim', 'sim']:
    respostas.append(c)
if d in ['s', 'S', 'Sim', 'sim']:
    respostas.append(d)
if e in ['s', 'S', 'Sim', 'sim']:
    respostas.append(e)

if len(respostas) == 2:
    print('Suspeita')
elif len(respostas) < 5:
    print('Cúmplice')
else:
    print('Assassino')
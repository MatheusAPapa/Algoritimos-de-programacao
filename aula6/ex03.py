def somaImposto(taxaImposto, custo):
    precoF = custo * (1 + taxaImposto)
    return precoF

produto1 = somaImposto(0.07, 100)
print(produto1)
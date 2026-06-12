QTD = 10

nomes = [''] * QTD
idades = [0] * QTD
soma = 0 

for i in range(QTD):
    nomes[i] = input('Nome: ')
    idades[i] = int(input('Idade: '))
    soma += idades[i]

media = soma / QTD

for i in range(QTD):
    if idades[i] > media:
        print(nomes[i])
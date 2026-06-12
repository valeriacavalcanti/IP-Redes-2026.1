cidades = [''] * 20
votos = [0] * 20

for i in range(20):
    cidades[i] = input('Cidade: ')
    votos[i] = 0

for i in range(100):
    voto = input('Cidade: ')

    j = cidades.index(voto)
    votos[j] += 1

for i in range(20):
    print(cidades[i], votos[i])
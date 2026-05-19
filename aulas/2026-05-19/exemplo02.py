numeros = [0] * 3
soma = 0
qtd_acima_media = 0

for i in range(len(numeros)):
    numeros[i] = int(input('Número: '))
    soma += numeros[i]

media = soma / len(numeros)

print(f'{soma = }')
print(f'{media = }')
print(f'{numeros = }')

# calcular quantidade de números com valor acima da média
for i in range(len(numeros)):
    if numeros[i] > media:
        qtd_acima_media += 1

print(f'{qtd_acima_media = }')

# exibir os números com valor acima da média
for i in range(len(numeros)):
    if numeros[i] > media:
        print(numeros[i])

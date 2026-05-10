soma = 0

for i in range(2):
    nota = float(input())
    while nota < 0 or nota > 10:
        print('nota invalida')
        nota = float(input())
    soma = soma + nota

media = soma / 2

print(f'media = {media:.2f}')

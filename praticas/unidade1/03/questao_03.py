def maior_valor(valor1: float, valor2: float) -> float:
    if (valor1 >= valor2):
        return valor1
    else:
        return valor2


## PP

idade1 = int(input('Idade: '))
altura1 = float(input('Altura: '))
peso1 = float(input('Peso: '))

idade2 = int(input('Idade: '))
altura2 = float(input('Altura: '))
peso2 = float(input('Peso: '))

maior_idade = maior_valor(idade1, idade2)
maior_altura = maior_valor(altura1, altura2)
maior_peso = maior_valor(peso1, peso2)

print(f'Maior idade: {maior_idade}')
print(f'Maior altura: {maior_altura}')
print(f'Maior peso: {maior_peso}')
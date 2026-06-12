import random

matriz = []
valores = []

for i in range(3):
    matriz.append([0] * 3)

for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(1, 50)

for i in range(3):
    for j in range(3):
        if matriz[i][j] not in valores:
            valores.append(matriz[i][j])

print(valores)
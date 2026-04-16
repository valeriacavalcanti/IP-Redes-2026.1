import random

sorteio = random.randint(0,100)
print(sorteio)

while True:
    chute = int(input('Número: '))

    if chute == sorteio:
        break

    if chute < sorteio:
        print('Seu chute é menor')
    else:
        print('Seu chute é maior')

print('acertou', chute, sorteio)

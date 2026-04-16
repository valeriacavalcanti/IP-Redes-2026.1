'''
'''

import random

numero = random.randint(0,100)
print(numero)

chute = int(input('Chute: '))

while chute != numero:
    print('Tá errado')
    if chute < numero:
        print('seu chute é menor')
    else:
        print('seu chute é maior')
    chute = int(input('Chute: '))

print('acertou', chute, numero)
    

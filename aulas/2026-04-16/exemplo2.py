'''
Programa para ler um número positivo ( > 0)
'''

num = int(input('Número: '))

while num <= 0:
    print('O número informado não é positivo')
    num = int(input('Número: '))

print(f'{num} é positivo')
print('Muito bem!')

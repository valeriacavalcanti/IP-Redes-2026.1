n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

maior = n1

if (n2 > maior):
    maior = n2

if (n3 > maior):
    maior = n3
    
print(f'{maior = }')
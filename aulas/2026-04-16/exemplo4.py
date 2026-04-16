'''
?
'''

print('1 - bom dia')
print('2 - boa tarde')
print('3 - boa noite')
print('0 - sair')
op = input('Digite sua opcao: ')

while op != '0':
    if op == '1':
        print('Bom dia')
    elif op == '2':
        print('Boa tarde')
    elif op == '3':
        print('Boa noite')
    else:
        print('Eita')

    op = input('Digite sua opcao: ')

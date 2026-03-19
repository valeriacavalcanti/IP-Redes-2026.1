nome = input('Digite seu nome: ')

idade = input('Digite sua idade: ')
idade = int(idade)

qtd_chocolate = int(input('Digite a quantidade de chocolates: '))

print('Seu nome é',nome)
#print('Seu nome é' + nome)
print('Sua idade é',idade)
print(qtd_chocolate)
#print()
print('Nome:', nome, '- Idade:', idade)

print(f'Nome: {nome}\nIdade: {idade}')
#print('Nome: {nome} - Idade: {idade}')

frase = f'Nome: {nome}\nIdade: {idade}'


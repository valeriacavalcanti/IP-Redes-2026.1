QTD = 4

arq = open('dados.txt', 'w')

for i in range(QTD):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    
    arq.write(f'{nome},{idade}\n')

arq.close()

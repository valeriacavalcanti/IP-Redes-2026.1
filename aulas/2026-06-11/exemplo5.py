# ler as informações que estão no arquivo

arq = open('dados.txt', 'r')
registros = arq.read().splitlines()
arq.close()

soma = 0

# registro é uma linha do arquivo
for i in range(len(registros)):
    nome, idade = registros[i].split(',')
    idade = int(idade)
    soma += idade
    
    print(i, registros[i], nome, idade)

media = soma / len(registros)

print(media)


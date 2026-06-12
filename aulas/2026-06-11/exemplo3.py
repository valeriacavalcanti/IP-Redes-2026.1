# ler as informações que estão no arquivo

arq = open('dados.txt', 'r')

conteudo = arq.read()
registros = conteudo.splitlines()

print(conteudo)
print(registros)

arq.close()

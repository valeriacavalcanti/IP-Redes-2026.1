# ler as informações que estão no arquivo

arq = open('dados.txt', 'r')

# registro é uma linha do arquivo
for registro in arq.read().splitlines():
    print(registro)

arq.close()

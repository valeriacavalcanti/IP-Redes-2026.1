nota = int(input('Digite sua nota: '))

# validar a nota
if ((nota >= 0) and (nota <= 100)):
    aumento = nota * 0.3
    nota = nota + aumento
    if (nota > 100):
        nota = 100
    print(f'Nota: {nota:.0f}')
else:
    print('Erro: Nota inválida (fora do intervalo)')

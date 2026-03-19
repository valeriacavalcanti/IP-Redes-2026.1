valor = float(input('Informe um valor: '))

if (valor >= 0):
    aumento = valor * 0.2
    valor = valor + aumento
    print(f'Valor com aumento: R$ {valor:.2f}')
else:
    print('Erro: valor inválido (negativo)')

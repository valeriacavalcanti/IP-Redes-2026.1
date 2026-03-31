from questao_03_funcoes import *

valor_unitario = float(input('Informe o valor unitário em dólar: '))
quantidade = int(input('Informe a quantidade comprada: '))

valor_compra_dolar = calcular_valor_compra(valor_unitario, quantidade)
valor_compra_real = converter_dolar_para_real(valor_compra_dolar)
taxa_importacao = calcular_imposto(valor_compra_dolar)
valor_final_real = calcular_valor_final(valor_compra_dolar)

print(f'Valor da compra (em dólar): {valor_compra_dolar}')
print(f'Valor da compra (em real): {valor_compra_real}')
print(f'Valor da taxa de importação (em real): {taxa_importacao}')
print(f'Valor final da compra (em real): {valor_final_real}')
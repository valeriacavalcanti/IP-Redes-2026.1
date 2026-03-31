from questao_03_funcoes import *

assert calcular_valor_compra(10, 10) == 100     # o valor da compra é em dolar
assert converter_dolar_para_real(100) == 500    # a conversão é para real
assert calcular_imposto(100) == 300             # o imposto é calculado em reais
assert calcular_valor_final(100) == 800         # o valor final é em reais

print('Testes realizados com sucesso!')
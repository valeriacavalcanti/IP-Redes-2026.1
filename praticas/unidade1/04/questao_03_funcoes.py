# calcular o valor da compra a partir do valor unitário e a quantidade comprada
def calcular_valor_compra(valor_unitario: float, qtd_comprada: int) -> float:
    return valor_unitario * qtd_comprada


# converter um valor de dólar para real. Considerando que 1 dólar vale 5 reais
def converter_dolar_para_real(valor_dolar: float) -> float:
    return valor_dolar * 5


# calcular o imposto de importação a partir do valor da compra em dólar.
# o valor do imposto deve ser convertido para real
def calcular_imposto(valor_compra: float) -> float:
    if valor_compra <= 50:
        imposto = valor_compra * 0.2
    else:
        imposto = valor_compra * 0.6
    return converter_dolar_para_real(imposto)


# calcular o valor final da compra, que é o somatório do valor da compra + imposto
def calcular_valor_final(valor_compra: float) -> float:
    return converter_dolar_para_real(valor_compra) + calcular_imposto(valor_compra)
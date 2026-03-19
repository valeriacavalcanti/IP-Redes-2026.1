# funcoes

def dia_da_semana(codigo_dia:int) -> str:
    dia_extenso = ''
    if codigo_dia == 0:
        dia_extenso = 'Domingo'
    elif codigo_dia == 1:
        dia_extenso = 'Segunda'
    elif codigo_dia == 2:
        dia_extenso = 'Terça'
    elif codigo_dia == 3:
        dia_extenso = 'Quarta'
    elif codigo_dia == 4:
        dia_extenso = 'Quinta'
    elif codigo_dia == 5:
        dia_extenso = 'Sexta'
    elif codigo_dia == 6:
        dia_extenso = 'Sábado'

    return dia_extenso

# testes
#print(dia_da_semana(0))
#print(dia_da_semana(1))
#print(dia_da_semana(2))
#print(dia_da_semana(3))
#print(dia_da_semana(4))
#print(dia_da_semana(5))
#print(dia_da_semana(6))
#print(dia_da_semana(7))


# Programa Principal

num = int(input('Digite o número do dia: '))
dia = dia_da_semana(num)
print(dia)

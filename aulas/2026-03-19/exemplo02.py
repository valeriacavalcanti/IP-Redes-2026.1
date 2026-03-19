def verifica_par_impar(num: int) -> str:
    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'

def verifica_par(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False


## testes
#print(verifica_par_impar(5))
#print(verifica_par_impar(8))
#print(verifica_par_impar(0))
#print(verifica_par_impar(-6))
#print(verifica_par_impar(-5))

#print(verifica_par(5))
#print(verifica_par(8))
#print(verifica_par(0))
#print(verifica_par(-6))
#print(verifica_par(-5))

# PP

numero = int(input('Digite um número: '))
print('Seu número é', verifica_par_impar(numero))


if (verifica_par(numero) == True):
    print('Seu número é PAR')
else:
    print('Seu número é ÍMPAR')


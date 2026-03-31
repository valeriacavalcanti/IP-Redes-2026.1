def somar_valores(num1: int, num2: int) -> int:
    return num1 + num2

def maior_valor(num1: int, num2: int) -> int:
    if num1 >= num2:
        return num1
    else:
        return num2

def exibir_valores(num1: int, num2: int):
    print(f'Primeiro número: {num1}')
    print(f'Segundo número: {num2}')

def mensagem_pt() -> str:
    return 'Olá, bem-vindo ao programa de operações matemáticas!'

def mensagem_en() -> str:
    return 'Hello, welcome to the math operations program!'

def exibir_mensagem(idioma: str):
    if idioma == 'pt':
        msg = mensagem_pt()
    else:
        msg = mensagem_en()
        
    print(msg)

## programa principal

exibir_mensagem('pt')

numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))

exibir_valores(numero1, numero2)

soma = somar_valores(numero1, numero2)
maior = maior_valor(numero1, numero2)

print(soma, maior)

temperatura = int(input('Temperatura: '))

if (temperatura < 10):
    print('Muito frio')
else:
    if (temperatura <= 15):
        print('Frio')
    else:
        if (temperatura <= 25):
            print('Agradável')
        else:
            if (temperatura <= 30):
                print('Quente')
            else:
                print('Muito Quente')
qt = int(input())

for i in range(qt):
    num = int(input())
    soma = 0
    for j in range(1, (num // 2) + 1):
        if (num % j == 0):
            soma += j
    if (soma == num):
        print(num, 'eh perfeito')
    else:
        print(num, 'nao eh perfeito')
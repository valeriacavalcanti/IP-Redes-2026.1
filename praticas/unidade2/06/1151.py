n = int(input())

n1, n2 = 1, 0

for i in range(n - 1):
    print(n2, end=' ')
    n1, n2 = n2, n1 + n2

print(n2)
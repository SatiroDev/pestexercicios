n = int(input('Digite um número: '))
soma = 0
for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print(f'A soma dos números divisíveis por 3 ou 5 de 1 até {n} foi de: {soma}')
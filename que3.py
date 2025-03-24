num = int(input('Digite um número: '))
soma = 0
for i in range(0, num+1, 2):
    soma += i
print(f'A soma dos números pares de 0 até {num} foi de: {soma}')